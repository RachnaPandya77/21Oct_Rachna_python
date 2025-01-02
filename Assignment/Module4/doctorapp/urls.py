from django.contrib import admin
from django.urls import path,include
from doctorapp import views

urlpatterns = [
    path('',views.index),
]