from django.test import TestCase
from django.urls import reverse
from category.models import Category


class CategoryTemplateRenderingTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="test_category", slug="test_category", is_main=True, status=1
        )

    def test_category_list_template_content(self):
        response = self.client.get(reverse('category_form'))
        self.assertContains(response, 'form')