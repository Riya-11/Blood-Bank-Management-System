from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class TestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_index(self):
        response = self.client.get(reverse('finddonor:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finddonor/index.html')

    def test_load_cities(self):
        response = self.client.get(reverse('finddonor:ajax_load_cities'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finddonor/dropdown.html')
