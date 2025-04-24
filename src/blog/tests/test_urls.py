from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import blogs, blog_detail


class BlogURLTest(TestCase):
    def test_blogs_urls_resolves_to_blogs_view(self):
        url = reverse('blogs')
        self.assertEqual(resolve(url).func, blogs)

    def test_blog_detail_url_resolves_to_blog_detail_view(self):
        url = reverse('blog_detail', kwargs={'pk': 1, 'slug': 'test-slug'})
        self.assertEqual(resolve(url).func, blog_detail)