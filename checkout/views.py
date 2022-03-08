from django.shortcuts import render

from .forms import MembershipForm


# Create your views here.

def checkout(request):


    order_form = MembershipForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)