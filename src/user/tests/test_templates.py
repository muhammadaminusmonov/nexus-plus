from django.test import Client
from django.urls import reverse
from django.test import TestCase
from user.models import User


class BlogTemplatesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.user_data = {
            'username': 'william',
            'firstname': 'William',
            'email': 'william@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }
        self.user = User.objects.create_user(username='william', password='strongpassword123')

    def test_user_register_template_content(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'Register')
        self.assertContains(response, 'form')

    def test_user_login_template_content(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Login Now')
        self.assertContains(response, 'form')

    def test_user_logout_redirects_to_home(self):
        self.client.login(username='william', password='strongpassword123')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.home_url)