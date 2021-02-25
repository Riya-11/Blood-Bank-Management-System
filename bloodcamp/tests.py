from django.test import TestCase

from .models import BloodCamp, BloodCampDonor, BloodVolunteer

from django.contrib.auth.models import User

from django.urls import reverse


#model testing

class TestModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        bloodcamp = BloodCamp.objects.create(location = "Chennai", status = 1)

        bloodcampdonor = BloodCampDonor.objects.create(firstname = "john",
        lastname = "cena", email = "john@gmail.com", phone = "7250073079",
        bloodcamp = bloodcamp, gender = "Male", blood = "O+")

        volunteer = BloodVolunteer.objects.create(name = "john",
        email="john@gmail.com", phone = "7250073079", landmark="iiits",
        gender = 'male', state = "AP", city = 'sri city', locality = 'tada',
        house = 'bigstay', bloodcamp = bloodcamp)


    def test_bloodcamp(self):
        bloodcamp = BloodCamp.objects.get(campid=1)
        self.assertEquals(bloodcamp.checkingbloodcamp(),'Chennai')

    def test_blooddonor(self):
        blooddonor = BloodCampDonor.objects.get(id=1)
        exepected_value = f'{blooddonor.firstname}, {blooddonor.email}, {blooddonor.phone}, {blooddonor.bloodcamp}'

        self.assertEquals(blooddonor.checkingdonor(),str(exepected_value))

    def test_volunteer(self):
        volunteer = BloodVolunteer.objects.get(id=1)
        exepected_value = f'{volunteer.name}, {volunteer.email}, {volunteer.phone}, {volunteer.bloodcamp}'

        self.assertEquals(volunteer.checkingvolunteer(),str(exepected_value))



#view testing


from django.test.client import Client

class UsersListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_volunteering(self):
        response = self.client.get(reverse('bloodcamp:volunteering'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/volunteerform.html')

    def test_volunteeringlist(self):
        response = self.client.get(reverse('bloodcamp:volunteer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/volunteer_list.html')

    def test_history(self):
        response = self.client.get(reverse('bloodcamp:history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/history.html')

    def test_camphome(self):
        response = self.client.get(reverse('bloodcamp:camphome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/camphome.html')

    def test_ongoing(self):
        response = self.client.get(reverse('bloodcamp:ongoing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/ongoing.html')

    def test_upcoming(self):
        response = self.client.get(reverse('bloodcamp:upcoming'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/upcoming.html')

    def test_newcamppage(self):
        response = self.client.get(reverse('bloodcamp:newcamppage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloodcamp/newcamp.html')

    # def test_newdonorpage(self):
    #     response = self.client.get(reverse('bloodcamp:newdonorpage'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'bloodcamp/newdonor.html')
