from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import Http404

from .forms import ProductForm
from .models import Product, Category


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse_lazy('mainapp:index')

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, 'products/delete.html', {'obj': obj})


def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=obj)
    success_url = reverse_lazy('mainapp:index')

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {
            'form': form,
            'obj': obj
        }
    )


def product_create(request):
    form = ProductForm()
    success_url = reverse_lazy('mainapp:index')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def category_list(request):
    query = Category.objects.all()

    return render(request, 'products/__catalog.html', {'categories': query})


def product_list(request, pk):
    query = get_list_or_404(Product, category=pk)
    page = request.GET.get('page')
    paginator = Paginator(query, 10)

    products = paginator.get_page(page)

    return render(request, 'products/list.html', {'products': products})


def product_detail_by_url_key(request, url_key):
    obj = get_object_or_404(Product, url_key=url_key)

    return render(request, 'products/detail.html', {'product': obj})
