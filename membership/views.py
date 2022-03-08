from django.shortcuts import render, redirect



# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'membership/membership.html')

def success(request):
    """ A view to return the success page """

    return render(request, 'membership/success.html')

