from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

# Create your views here.

default_data = {
    'email': 'k@kml.email',
    'address': 'Berlin, Deutschland',
    'phone': '+49 000 00000000',
}


def main(request):
    template = get_template('mainapp/index.html')
    context = {
        **default_data,
        'page_type': 'home',
    }
    response_string = template.render(context)

    return HttpResponse(response_string)


def contacts(request):
    context = {
        **default_data,
        'page_type': 'contacts',
    }
    response_string = render_to_string(
        'mainapp/contacts.html',
        context
    )

    return HttpResponse(response_string)

