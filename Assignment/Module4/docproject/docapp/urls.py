from django.contrib import admin
from django.urls import path,include
from docapp import views

urlpatterns = [
    path('',views.index),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
]