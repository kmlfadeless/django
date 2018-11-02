from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import AccountUserForm, RegisterUserForm
from .models import AccountUser


def account_login(request):
    success_url = reverse_lazy('mainapp:index')
    form = AccountUserForm()

    if request.method == 'POST':
        form = AccountUserForm(data=request.POST)

        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(
                username=usr,
                password=pwd,
            )

            # чтобы предотвратить обнаружение аккаунтов суперюзеров,
            # исключим их из авторизации на форме
            print(usr)
            print(pwd)
            if user and user.is_active and not user.is_superuser:
                print("here ok")
                login(request, user)

                return redirect(success_url)

    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    form = RegisterUserForm()

    if request.method == "POST":
        postdata = request.POST.copy()
        username = postdata.get('username', '')
        password = postdata.get('password', '')

        # check if user does not exist
        if AccountUser.objects.filter(username=username).exists():
            username_unique_error = True

        else :
            create_new_user = AccountUser.objects.create_user(username, '', password)
            create_new_user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            if create_new_user is not None:
                if create_new_user.is_active:
                    return HttpResponseRedirect('/profile')
                else:
                    print("The password is valid, but the account has been disabled!")

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
