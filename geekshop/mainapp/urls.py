from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    main, contacts,
)

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='index'),
    path('contacts', contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
