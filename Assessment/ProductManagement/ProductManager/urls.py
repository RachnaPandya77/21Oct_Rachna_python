from django.urls import path
from . import views

urlpatterns = [
    path('register_product/', views.register_product, name='register_product'),
    path('view_products/', views.view_products, name='view_products'),
]