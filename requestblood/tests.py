from django.test import TestCase

# Create your tests here.

from home.models import State, City

from .models import Requestor

from django.urls import reverse

from django.shortcuts import redirect

class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        state = State.objects.create(name = 'Bihar')
        city = City.objects.create(name='Patna', state = state)
        requester = Requestor.objects.create(name ="john",
        blood ="A+", state=state, city=city,
        phone = 7250073079, email="raybittu242@gmail.com",reason="Fever")

    def test_requestor(self):
        requestor = Requestor.objects.get(id=1)
        exepected_value = f'{requestor.name}, {requestor.phone}, {requestor.email}, {requestor.reason}'
        self.assertEquals(requestor.checkingrequestor(),str(exepected_value))


class TestViewRequestor(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    # def test_index(self):
    #      response = self.client.get(redirect(1,reverse('requestblood:index')))
    #      self.assertEqual(response.status_code, 200)
    #      self.assertTemplateUsed(response, 'requestblood/index.html')

    def test_sorry(self):
        response = self.client.get(reverse('requestblood:sorry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requestblood/index.html')


    def test_response(self):
        response = self.client.get(reverse('requestblood:response'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requestblood/index.html')


    def test_red(self):
        response = self.client.get(reverse('requestblood:red'))
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'requestor/sorry.html')
        self.assertRedirects(response, '/availability/')
