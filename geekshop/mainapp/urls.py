from django.urls import path

from .views import (
    main, contacts,
)

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='index'),
    path('contacts', contacts, name='contacts'),
]