from django.shortcuts import render


# Create your views here.

def order(request):
    context = {}
    return render(request, 'store/order.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
