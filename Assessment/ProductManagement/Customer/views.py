from django.shortcuts import render, redirect
from .models import Customer, Order
from ProductManager.models import Product
from .forms import CustomerForm, OrderForm

# Create your views here.

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_login')
    else:
        form = CustomerForm()
    return render(request, 'register_customer.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        customer = Customer.objects.filter(email=email).first()
        if customer:
            return redirect('view_products')
    return render(request, 'customer_login.html')

def purchase_product(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
             form.save()
        return redirect('view_orders')
    else:
        form = OrderForm()
    return render(request, 'purchase_product.html', {'form': form})

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'view_orders.html', {'orders': orders})
