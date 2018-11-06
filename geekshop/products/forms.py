from django.forms import ModelForm

from .models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'alt', 'name',
            'description', 'characteristics', 'details',
            'url_key', 'category'
        ]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'snippet']
