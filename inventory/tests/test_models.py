from django.test import TestCase
from inventory.models import Category, Product
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(
            name = "django", slug="django"
        )

    def test_category_model_entry(self):
        data1 = self.data1
        self.assertTrue(isinstance(data1, Category))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), "django") #And here when we take the string of the data it is going to return the name

class TestProductModel(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="Admin")
        self.data1 = Product.objects.create(
            category_id=1, created_by_id=1, title="django Book", slug="django Book",
            price="20.00"
        )#The thing to note here is about the foreign keys, instead of putting the name we are going to
        # take the id of the foreign keys

    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django Book")
