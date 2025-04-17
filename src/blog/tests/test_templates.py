from django.test import TestCase
from blog.models import Blog


class TestBlogsTemplates(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create()


class TestBlogDetailTemplate():
    pass