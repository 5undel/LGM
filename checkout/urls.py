from django.contrib import admin
from django.urls import path
from . import views

# path for the checkout and success page
urlpatterns = [
    path('<int:pk>/', views.checkout, name='checkout'),
    path('checkout_success/<membership_number>', views.checkout_success, name='checkout_success'),
]
