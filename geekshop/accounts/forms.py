from django import forms


class AccountUserForm(forms.Form):
    username = forms.CharField(
        label='Login', max_length=150,
    )
    password = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput()
    )


class RegisterUserForm(forms.Form):
    username = forms.CharField(
        label='Login', max_length=150,
    )
    password = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput()
    )
