from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user.models import Profile


class UserViewsTest(TestCase):
    def setUp(self):
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

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post_valid_data_creates_user_and_redirects(self):
        response = self.client.post(self.register_url, self.user_data)
        # print(response.context['form'].errors)
        self.assertRedirects(response, self.home_url)

        user = User.objects.get(username='william')
        self.assertTrue(user)
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_valid_credentials_redirects(self):
        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, {
            'username': 'william',
            'password': 'strongpassword123',
        })
        self.assertRedirects(response, self.home_url)

    def test_logout_view_redirect_to_home(self):
        self.client.post(self.register_url, self.user_data)
        self.client.login(username='william', password='strongpassword123')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.home_url)