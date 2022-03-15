from django.shortcuts import render


# Create your views here.
def all_products(request):
    """ A view to return the membership page """

    

    context = {}

    return render(request, 'crossfit/crossfit.html', context)