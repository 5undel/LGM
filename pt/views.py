from django.shortcuts import render, redirect, get_object_or_404
from .models import Coach


# Create your views here.
def all_coachs(request):
    """ A view to return the pt page """

    coachs = Coach.objects.all()

    context = {
        'coachs' : coachs,
    }

    return render(request, 'pt/pt.html', context)


def coach_detail(request, coach_id):
    """ A view to return the pt detail page """

    coach = get_object_or_404(Coach, pk=coach_id)

    context = {
        'coach' : coach,
    }

    return render(request, 'pt/coach_detail.html', context)