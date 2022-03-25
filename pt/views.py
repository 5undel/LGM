from django.shortcuts import render, redirect, get_object_or_404
from .models import Coach
from django.contrib import messages
from django.conf import settings

from .forms import BookingForm
from .models import Coach


# Create your views here.
def all_coachs(request):
    """ A view to return the pt page """

    coachs = Coach.objects.all()

    context = {
        'coachs': coachs,
    }

    return render(request, 'pt/pt.html', context)


def coach_detail(request, coach_id):
    """ A view to return the pt detail page """

    coach = get_object_or_404(Coach, pk=coach_id)


    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            order = booking_form.save()
            order.save()

    booking_form = BookingForm()
    context = {
        'coach': coach,
        'booking_form': booking_form,
    }

    return render(request, 'pt/coach_detail.html', context)


def pt_success(request):
    """ A view to return the pt page """

    coach = Coach

    context = {
        'coach': coach,
    }

    return render(request, 'pt/pt_success.html', context)
