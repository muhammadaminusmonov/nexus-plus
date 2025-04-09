from django.test import TestCase
from region.models import Region

class RegionModelTest(TestCase):
    def test_Region(self):
        region = Region.objects.create(name='Test Region', sorting=1)
        self.assertEqual(region.name, 'Test Region')
        self.assertEqual(region.sorting, 1)