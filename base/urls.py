from django.contrib import admin
from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('', views.index, name='home'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('contact', views.contact, name='contact'),
]
