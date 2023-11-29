from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    return render(request, "inventory/home.html", {"products":products})
