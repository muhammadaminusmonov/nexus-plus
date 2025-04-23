from django.test import TestCase
from django.contrib.auth.models import User
from user.models import Profile
from user.forms import RegisterForm, LoginForm


class RegisterFormTest(TestCase):

    def setUp(self):
        self.valid_data = {
            'username': 'william',
            'firstname': 'William',
            'email': 'william@gmail.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

    def test_register_form_valid_data(self):
        form = RegisterForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_register_form_password_do_not_match(self):
        data = self.valid_data.copy()
        data['password2'] = 'worongpassword'
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_register_form_missing_required_field(self):
        data = self.valid_data.copy()
        del data['email']
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_register_form_creates_user_and_profile(self):
        form = RegisterForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(User.objects.filter(username=user.username).exists())
        self.assertTrue(Profile.objects.filter(user=user).exists())
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.firstname, 'William')

class LoginFormTest(TestCase):

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username': 'william',
            'password': 'testpass',
        })
        self.assertTrue(form.is_valid())

    def test_login_form_missing_username(self):
        form = LoginForm(data={
            'password': 'testpass'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_login_form_missing_password(self):
        form = LoginForm(data={
            'username': 'testuser'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)