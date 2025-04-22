from django.test import TestCase
from django.urls import reverse, resolve
from user.views import register_view, login_view, logout_view

class UserURLTest(TestCase):
    def test_register_url_resolves_to_register_view(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

    def test_login_url_resolves_to_login_view(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_url_resolves_to_logout_view(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_view)
