from django.urls import path

from .views import (
    main, contacts,
)

urlpatterns = [
    path('', main),
    path('contacts', contacts),
]