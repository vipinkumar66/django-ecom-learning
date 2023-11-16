from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug':('name',)} #we dont have to give the slug field manually
    # As we enter the title it will automatically generate the slug for it

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","author", "slug", "price", "in_stock", "created", "updated"]
    list_filter = ["in_stock", "is_active"]
    list_editable = ["price", "in_stock"]
    prepopulated_fields = {"slug": ("title",)}