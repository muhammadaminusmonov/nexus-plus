from django.test import TestCase, Client
from blog.models import Blog, BlogComment
from django.contrib.auth.models import User
from user.models import Profile
from category.models import Category
from django.urls import reverse

class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.profile = Profile.objects.create(user=self.user)
        self.parent_category = Category.objects.create(name='testparent', status=2)
        self.child_category = Category.objects.create(name='AI', parent=self.parent_category, status=2)
        for i in range(6):
            Blog.objects.create(
                title=f'Blog {i}',
                content='Some content',
                user=self.profile,
                category=self.parent_category,
            )
        self.blog = Blog.objects.first()
        self.blog_detail_url = reverse('blog_detail', kwargs={'pk': self.blog.pk, 'slug': self.blog.slug})
        self.blogs_url = reverse('blogs')

    def test_blogs_view_template_and_context(self):
        response = self.client.get(self.blogs_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs.html')

        # Check pagination
        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 3)  # per page=3

        # Check other context variables
        self.assertIn('categories', response.context)
        self.assertIn('recent_blogs', response.context)
        self.assertIn('page_number', response.context)

    def test_blog_detail_view_template_and_context(self):
        # Add a comment and a reply
        comment = BlogComment.objects.create(user=self.profile, blog=self.blog, comment='Nice!')
        BlogComment.objects.create(user=self.profile, blog=self.blog, comment='Thanks!', reply=comment)

        response = self.client.get(self.blog_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')

        # Check context data
        self.assertIn('blog', response.context)
        self.assertEqual(response.context['blog'].pk, self.blog.pk)

        self.assertIn('categories', response.context)
        self.assertIn('replies', response.context)
        self.assertGreaterEqual(response.context['replies'].count(), 1)
        self.assertIn('recent_blogs', response.context)