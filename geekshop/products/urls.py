from django.urls import path

from .views import (
    category_list, product_list, product_detail_by_url_key
)

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', product_list, name='category'),
    path('<str:url_key>/', product_detail_by_url_key, name='url_key'),
    path('', category_list, name='index'),
]