from django.urls import path

from .views import account_login, register, profile


app_name = 'accounts'


urlpatterns = [
    path('', account_login, name='login'),
    path('login/', account_login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]