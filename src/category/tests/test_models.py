from django.test import TestCase
from category.models import Category, Brand


class CategoryModelTest(TestCase):

    def test_create_main_category(self):
        category = Category.objects.create(
            name='Electronics',
            is_main=True,
            slug='electronics',
        )
        self.assertEqual(category.name, 'Electronics')
        self.assertEqual(category.slug, 'electronics')
        self.assertTrue(category.is_main)
        self.assertIsNone(category.parent)

    def test_create_sub_category(self):
        parent = Category.objects.create(name='Electronics', slug='electronics')
        sub = Category.objects.create(
            name='Phones',
            slug='phones',
            parent=parent,
        )
        self.assertEqual(sub.parent, parent)

class BrandModelTest(TestCase):
    def test_create_brand(self):
        brand = Brand.objects.create(name="Test Brand")
        self.assertEqual(brand.name, "Test Brand")