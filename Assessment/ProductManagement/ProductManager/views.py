from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()
    return render(request, 'register_product.html', {'form': form})

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})