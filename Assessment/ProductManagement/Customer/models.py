from django.db import models
from ProductManager import Product

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    city  = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"
