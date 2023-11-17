from django.test import TestCase
from inventory.models import Category, Product

class TestCategoryModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(
            name = "Django", slug="django"
        )

    def test_category_model_entry(self):
        data1 = self.data1
        self.assertTrue(isinstance(data1, Category))