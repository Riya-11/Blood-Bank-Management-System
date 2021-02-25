from django.test import TestCase

from home.models import State,City,UserAddress,UserProfile,UserHistory

from django.contrib.auth.models import User

from django.urls import reverse

# Create your tests here.

#model testing

class TestSateCityModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        state = State.objects.create(name = 'Bihar')
        City.objects.create(name='Patna', state = state)

    def test_state(self):
        state = State.objects.get(id = 1)
        self.assertEquals(state.checkingstate(),'Bihar')

    def test_city(self):
        city = City.objects.get(id = 1)

        exepected_value = f'{city.name}, {city.state.name}'

        self.assertEquals(city.checkingcity(),str(exepected_value))


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username = 'bitturay',first_name = 'bittu' ,last_name = 'ray',
        email = 'raybittu242@gmail.com',password = '12345bittu')

        state = State.objects.create(name = 'Bihar')
        city = City.objects.create(name='Patna', state = state)

        useraddress = UserAddress.objects.create(user = user, state = state,
        city = city, phone = 7250073079467, locality = 'Bihar', house = 'Bigstay',
        landmark = 'IIIT Sri City', birth = '1998-10-10', gender = 'Male', blood = 'O+')

        userprofile = UserProfile.objects.create(user = user, status = 'Never give up and work hard')

    def test_user(self):
        useraddress = UserAddress.objects.get(useraddressid = 1)
        #print(useraddress.phone)

        exepected_value = f'{useraddress.user.username}, {useraddress.user.email}, {useraddress.phone}'
        self.assertEquals(useraddress.checkinguser(),str(exepected_value))

    def test_maxlength(self):
        useraddress = UserAddress.objects.get(useraddressid = 1)
        max_length = useraddress._meta.get_field('phone').max_length

        #exepected_value = f'{useraddress.user.username}, {useraddress.user.email}'
        self.assertEquals(max_length,10)

    def test_userprofile(self):
        userprofile = UserProfile.objects.get(userprofileid = 1)
        #print(useraddress.phone)

        exepected_value = f'{userprofile.user.username}, {userprofile.status}'
        self.assertEquals(userprofile.checkinguserprofile(),str(exepected_value))







#views template testing
from django.test.client import Client

class UsersListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='john',
        email='lennon@thebeatles.com', password='johnpassword')


    def test_view_uses_correct_template_index(self):
            response = self.client.get(reverse('home:index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'home/index.html')

    def test_view_uses_correct_template_faqs(self):
            response = self.client.get(reverse('home:faq'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'home/faq.html')


    def test_view_uses_correct_template_signup(self):
            response = self.client.get(reverse('home:signup'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'home/signup.html')

    def test_view_uses_correct_template_login(self):
            response = self.client.get(reverse('home:login'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'home/login.html')


#url views testing


    def test_view_url_accessible_by_name_profile(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('home:profile'))
        self.assertTemplateUsed(response, 'home/profile.html')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_about(self):
        #self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_view_url_accessible_by_name_logout(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('home:user_logout'))
        #self.assertTemplateUsed(response, 'home/index.html')
        self.assertRedirects(response, '/home/')


    def test_view_url_accessible_by_name_imageupload(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('home:image_upload'))
        self.assertRedirects(response, '/home/profile/')
        #self.assertTemplateUsed(response, 'home/uploadedpic.html')

    def test_view_url_accessible_by_name_updatedetails(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('home:update_details'))
        #self.assertTemplateUsed(response, 'home/update_details.html')
        self.assertRedirects(response, '/home/profile/')


    def test_view_url_accessible_by_name_updatedepassword(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('home:update_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/password.html')
