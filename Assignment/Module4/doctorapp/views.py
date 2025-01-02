from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        d=doc(request.POST)
        if d.is_valid():
            d.save()
            print("Data inserted")
        else:
            print(d.errors)
    return render(request,'index.html')

