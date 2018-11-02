from django.urls import path

from .views import (
    category_list, product_list, product_detail_by_url_key,
    product_create, product_update, product_delete
)

app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', product_delete, name='delete'),
    path('<int:pk>/update/', product_update, name='update'),
    path('create/', product_create, name='create'),
    path('<int:pk>/', product_list, name='category'),
    path('<str:url_key>/', product_detail_by_url_key, name='url_key'),
    path('', category_list, name='index'),
]