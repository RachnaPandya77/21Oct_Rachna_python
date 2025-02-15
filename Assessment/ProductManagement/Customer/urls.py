from django.urls import path
from . import views

urlpatterns = [
    path('register_customer/', views.register_customer, name='register_customer'),
    path('customer_login/', views.customer_login, name='customer_login'),
    path('purchase_product/', views.purchase_product, name='purchase_product'),
    path('view_orders/', views.view_orders, name='view_orders'),
]