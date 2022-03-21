from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_coachs, name='pt'),
    path('<coach_id>', views.coach_detail, name='coach_detail'),
]