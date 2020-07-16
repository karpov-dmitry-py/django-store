from django.shortcuts import render

def store(request):
    context = {
        'title': 'This is store',
        'body': 'This is store page',
    }
    return render(request, 'store/store.html', context)

def cart(request):
    context = {
        'title': 'This is cart',
        'body': 'This is cart page',
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {
        'title': 'This is checkout',
        'body': 'This is checkout page',
    }
    return render(request, 'store/checkout.html', context)