from django.test import TestCase

# Create your tests here.
from .models import PathLabUser2

from django.urls import reverse

from home.models import UserProfile

from django.contrib.auth.models import User


class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="john",
        password = "abcd123")
        userprofile = UserProfile.objects.create(user=user)
        pathuser2 = PathLabUser2.objects.create(profile = userprofile,
        firstname="john",lastname="cena",address="Patna",
        bloodgroup="A+",testtype="first")

    def test_pathlabuser2(self):
        pathuser2 = PathLabUser2.objects.get(id=1)
        self.assertEquals(pathuser2.firstname,"john")
        self.assertEquals(pathuser2.lastname,"cena")
        self.assertEquals(pathuser2.address,"Patna")
        self.assertEquals(pathuser2.bloodgroup,"A+")
        self.assertEquals(pathuser2.testtype,"first")

from django.test.client import Client
class TestViewPathUser2(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        user = User.objects.create_user(username='john',
        email='lennon@thebeatles.com', password='johnpassword')
        userprofile = UserProfile.objects.create(user=user)
        pathuser2 = PathLabUser2.objects.create(profile = userprofile,
        firstname="john",lastname="cena",address="Patna",
        bloodgroup="A+",testtype="first")


    def test_index(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('pathlab:index'))
        self.assertTemplateUsed(response, 'pathlab/index.html')
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('pathlab:result'))
        self.assertTemplateUsed(response, 'pathlab/result.html')
        self.assertEqual(response.status_code, 200)

    def test_booko(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('pathlab:booko'))
        self.assertTemplateUsed(response, 'pathlab/booko.html')
        self.assertEqual(response.status_code, 200)

    def test_history(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('pathlab:history'))
        self.assertTemplateUsed(response, 'pathlab/history.html')
        self.assertEqual(response.status_code, 200)

    # def test_report(self):
    #     self.client.login(username='john', password='johnpassword')
    #     response = self.client.get(reverse('pathlab:report',args=[]))
    #     self.assertTemplateUsed(response, 'pathlab/report.html')
    #     self.assertEqual(response.status_code, 200)
