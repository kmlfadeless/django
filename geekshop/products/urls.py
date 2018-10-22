from django.urls import path

from .views import (
    product_list, product_detail
)


urlpatterns = [
    path('<int:idx>', product_detail),
    path('', product_list),
]