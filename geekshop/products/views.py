from django.shortcuts import render

from .models import Product, Category


def category_list(request):
    query = Category.objects.all()

    return render(request, 'products/catalog.html', {'categories': query})


def product_list(request, pk):
    query = Product.objects.filter(category=pk)

    return render(request, 'products/category.html', {'products': query})


def product_detail_by_url_key(request, url_key):
    obj = Product.objects.get(url_key=url_key)

    return render(request, 'products/detail.html', {'product': obj})
