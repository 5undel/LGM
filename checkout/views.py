from django.shortcuts import render

from .forms import MembershipForm


# Create your views here.

def checkout(request):


    order_form = MembershipForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kam1sBZywz1S249sDKthLEziMimVdDqC5Dc9u8J3FrU205CISNTJJeQN87UOJLbqa59ok1EtG2iY5hHzkowNt1600OQ9zjTgm',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)