from django.shortcuts import render
from django.conf import settings
from .forms import MembershipForm


import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLICE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = 5*1000,
        currency = settings.STRIPE_CURRENCY,
    )
    order_form = MembershipForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)