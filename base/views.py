from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'base/index.html')


def userlogin(request):
    """ A view to return the user login page """

    return render(request, 'base/userlogin.html')

def contact(request):
    """ A view to return the contact page """

    return render(request, 'base/contact.html')
