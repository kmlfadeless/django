from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def iPhone5c(request):
    return render(request, 'mainapp/iPhone5c.html')


def iPhoneX(request):
    return render(request, 'mainapp/iPhoneX.html')
