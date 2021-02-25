from django.test import TestCase

# Create your tests here.

from django.urls import reverse

class TestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_index(self):
        response = self.client.get(reverse('display:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'display/index.html')
