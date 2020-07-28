from django.shortcuts import render
from .models import *


def store(request):
    context = {
        'title': 'This is store',
        'body': 'This is store page',
        'products': Product.objects.all(),
    }
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.items.all()
    else:
        items = []  # TODO - implement logic later
        order = None

    context = {
        'title': 'This is cart',
        'body': 'This is cart page',
        'order': order,
        'items': items,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {
        'title': 'This is checkout',
        'body': 'This is checkout page',
    }
    return render(request, 'store/checkout.html', context)
