from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.all_products, name="all_products"),
    path("item/<slug:slug>", views.product_detail, name="product_detail"),
    # Lets write a category serach url: Bascically when ever we will be searching a category at that time
    # we will be getting all the products related to that category
    path("search/<slug:category_slug>", views.category_list, name="category_list"),
]