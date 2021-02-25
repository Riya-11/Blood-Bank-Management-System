from django.test import TestCase

# Create your tests here.

from .models import PathlabName, BloodBankName

from django.urls import reverse


class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        bloodbank = BloodBankName.objects.create(bloodbankname="Chennai",
        latitude=26.37,longitude=54.76)
        pathlab = PathlabName.objects.create(pathlabname="Kolkata",
        latitude=52.67,longitude=25.84)

    def test_bloodbankname(self):
        bloodbank = BloodBankName.objects.get(bloodbankid = 1)
        self.assertEquals(bloodbank.bloodbankname,"Chennai")
        self.assertEquals(bloodbank.longitude,54.76)
        self.assertEquals(bloodbank.latitude,26.37)

    def test_pathlabname(self):
        pathlab = PathlabName.objects.get(pathlabid=1)
        self.assertEquals(pathlab.latitude,52.67)
        self.assertEquals(pathlab.longitude,25.84)
        self.assertEquals(pathlab.pathlabname,"Kolkata")




from django.test.client import Client

class MapsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_index(self):
        response = self.client.get(reverse('maps:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps/map.html')

    def test_index1(self):
        response = self.client.get(reverse('maps:pathlab'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps/map1.html')
