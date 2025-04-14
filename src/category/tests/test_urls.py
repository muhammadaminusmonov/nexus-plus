from django.test import TestCase
from django.urls import resolve, reverse
from category.views import category_form


class CategoryURLTest(TestCase):
    def test_category_list_url_resolves(self):
        url = reverse('category_form')
        self.assertEqual(resolve(url).func, category_form)