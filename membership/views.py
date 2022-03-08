from django.shortcuts import render, redirect
from .models import Product



# Create your views here.
def all_products(request):
    """ A view to return the index page """

    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'membership/membership.html', context)


