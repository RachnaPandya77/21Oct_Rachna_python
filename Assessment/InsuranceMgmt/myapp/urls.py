from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
     path('',views.index),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    
]
