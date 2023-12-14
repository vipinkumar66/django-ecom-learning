from django.shortcuts import render
from .basket import Basket
from inventory.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
def basket_summary(request):
    return render (request, "inventory/basket/summary.html")

def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        return JsonResponse({"qty":product_qty})
