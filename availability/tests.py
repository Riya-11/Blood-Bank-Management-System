from django.test import TestCase

# Create your tests here.

from django.urls import reverse

from .models import BloodAvailability

from django.test.client import Client

#model Test

class TestModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        blood = BloodAvailability.objects.create(threshold = 10, quantity = 20, blood = 'A')

    def test_blood(self):
        blood = BloodAvailability.objects.get(id=1)
        exepected_value = f'{blood.threshold}, {blood.quantity}, {blood.blood}'
        self.assertEqual(blood.chekingblood(), str(exepected_value), 'BloodAvailability model failed')


#view test


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_uses_correct_template_index(self):
            response = self.client.get(reverse('availability:index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'availability/index.html')
