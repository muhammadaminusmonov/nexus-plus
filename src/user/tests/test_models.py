from django.test import TestCase
from user.models import Profile
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='william', password='arthur')
        self.profile = Profile.objects.create(
            user=self.user,
            firstname='William',
            lastname='Arthur',
            phone='998776665544',
            address='123 Main St',
            bio='This is the bio',
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.firstname, 'William')
        self.assertEqual(self.profile.lastname, 'Arthur')
        self.assertEqual(self.profile.phone, '998776665544')
        self.assertEqual(self.profile.address, '123 Main St')
        self.assertEqual(self.profile.bio, 'This is the bio')
        self.assertEqual(str(self.profile), 'William Arthur')
        self.assertEqual(self.profile.user.username, 'william')