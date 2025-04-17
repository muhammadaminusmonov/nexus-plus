from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog, BlogComment
from category.models import Category
from user.models import Profile


class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.profile = Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name='test', status=2, slug='test')
        self.blog = Blog.objects.create(user=self.profile, category=self.category, title='test title', content='test content', slug='test-slug')

    def test_blog_creation(self):
        self.assertEqual(self.blog.title, 'test title')
        self.assertEqual(self.blog.content, 'test content')
        self.assertEqual(self.blog.slug, 'test-slug')
        self.assertEqual(str(self.blog), 'test title')
        self.assertIsNotNone(self.blog.created_at)
        self.assertIsNotNone(self.blog.updated_at)

    def test_blog_slug_generation_on_save(self):
        blog = Blog.objects.create(user=self.profile, category=self.category, title='test title', content='test content')
        self.assertEqual(blog.slug, 'test-title')


class BlogCommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.profile = Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name='test', status=2, slug='test')
        self.blog = Blog.objects.create(user=self.profile, category=self.category, title='test title', content='test content')
        self.comment = BlogComment.objects.create(blog=self.blog, user=self.profile, comment='test content')

    def test_comment_creation(self):
        self.assertEqual(self.comment.blog.title, 'test title')
        self.assertEqual(self.comment.blog.content, 'test content')
        self.assertEqual(self.comment.blog, self.blog)

    def test_reply_to_comment(self):
        reply = BlogComment.objects.create(blog=self.blog, user=self.profile, comment='test content', reply=self.comment)
        self.assertEqual(reply.reply, self.comment)
        self.assertIn(reply, self.comment.replies.all())