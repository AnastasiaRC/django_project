from django.shortcuts import render
from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    context = {
        'odject_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
