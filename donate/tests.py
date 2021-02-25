from django.test import TestCase

# Create your tests here.

from django.urls import reverse

from .models import Appointment

from django.contrib.auth.models import User

from django.test.client import Client


class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="bitturay123",password="12345ray")
        appointement = Appointment.objects.create(user=user, reference_no="abd1424",
        pathlab = "Chennai")

    def test_appointement(self):
        appointement = Appointment.objects.get(id = 1)
        exepected_value = f'{appointement.user.username}, {appointement.reference_no}'
        self.assertEquals(appointement.checkingappointment(),str(exepected_value))



class TestViewAppointement(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='john',
        email='lennon@thebeatles.com', password='johnpassword')


    def test_index(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('donate:index'))
        self.assertTemplateUsed(response, 'donate/index.html')
        self.assertEqual(response.status_code, 200)


    def test_thanks(self):
        response = self.client.get(reverse('donate:thanks'))
        self.assertTemplateUsed(response, 'donate/thanks.html')
        self.assertEqual(response.status_code, 200)
