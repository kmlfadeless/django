from django.urls import path

from mainapp.views import (
    main, contacts, catalog, iPhone5c, iPhoneX
)

urlpatterns = [
    path('', main),
    path('contacts', contacts),
    path('catalog', catalog),
    path('iPhoneX', iPhoneX),
    path('iPhone5c', iPhone5c),
]