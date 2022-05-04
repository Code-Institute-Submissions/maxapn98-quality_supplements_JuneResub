from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ko1E3KJytdeHtX1V3K9lRl1PBLrfXU5PBVIhB0Y6dh6uSr6yfqXtfGKtlbeeF35fuAHdU0AtbKCxmPtGE55CEfE004fYeVjbj',
        'client_secret': 'test client secret',        
    }

    return render(request, template, context)