from django.test import TestCase
from django.urls import reverse, resolve
from django.template.loader import render_to_string
from category.models import Category
from category.forms import CategoryForm
from category.views import category_form

class CategoryViewTest(TestCase):

    def setUp(self):  # Corrected method name
        self.category = Category.objects.create(
            name="test", slug="test", is_main=True
        )

    def test_category_list_view_status_code(self):
        response = self.client.get(reverse("category_form"))
        self.assertEqual(response.status_code, 200)

    def test_category_list_view_template_used(self):
        response = self.client.get(reverse("category_form"))
        self.assertTemplateUsed(response, "category_form.html")

    def test_category_list_view_context(self):
        response = self.client.get(reverse("category_form"))
        # self.assertIn(self.category, response.context["name"])