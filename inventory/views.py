from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def get_categories(request):
    """
    This one is used in the context in the settings
    """
    return {"categories": Category.objects.all()}

def all_products(request):
    """
    Here the context is directly passed to the templates and than used
    """
    products = Product.objects.all()
    return render(request, "inventory/home.html", {"products":products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    # This get_object_or_404 (we need to pass the model and the filters or requirements) as we gave here
    return render(request, "inventory/products/detail.html", {'product':product})