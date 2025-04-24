from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from user.models import Profile
from category.models import Category
from blog.models import Blog, BlogComment


class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='william', password='123456')
        self.profile = Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name='Tech', slug='tech', status=2)
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='some content',
            slug='test-blog',
            category=self.category,
            user=self.profile,
        )
        self.comment = BlogComment.objects.create(
            user=self.profile,
            blog=self.blog,
            comment='some comment',
        )
        self.reply = BlogComment.objects.create(
            user=self.profile,
            blog=self.blog,
            comment='some reply',
            reply=self.comment,
        )

    def test_blogs_view_status_code(self):
        url = reverse('blogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs.html')

    def test_blogs_view_context(self):
        url = reverse('blogs')
        response = self.client.get(url)
        self.assertIn('page_obj', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('recent_blogs', response.context)

    def test_blog_detail_status_code(self):
        url = reverse('blog_detail', kwargs={'pk':self.blog.pk, 'slug': self.blog.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')

    def test_blog_detail_context(self):
        url = reverse('blog_detail', kwargs={'pk':self.blog.pk, 'slug': self.blog.slug})
        response = self.client.get(url)
        self.assertIn('blog', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('recent_blogs', response.context)
        self.assertIn('replies', response.context)