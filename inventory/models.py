from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        # Just to provide the additional info about the data points
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        # To represent the data properly
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    # Foreign key is to do the work of many to one relationship
    # Related name is to do the reverse relationship easy. Category.product_set.all() without the related name
    # and with it: Category.prooduct.all()
    created_by = models.ForeignKey(User, related_name="product_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "products"
        ordering = ("-created",) #last item that is added is returned first and this can be written as tuples or list

    def get_absolute_url(self):
        """
        The reverse function helps to generate the url for the given view, here it takes the
        url name and additonaly we can pass the args that we want to attach in the url
        """
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title
