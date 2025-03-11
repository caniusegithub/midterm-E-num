from django.shortcuts import render

# Create your views here.

from .models import Product

def product_list(request):
    products = Product.objects.all().order_by("name")
    return render(request, "merchstore/product_list.html", {"products": products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id) 
    return render(request, "merchstore/product_detail.html", {"product": product})