from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import Wallet, Transaction

from django.contrib.auth.models import User

#model testing

# class TestModel(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#
#         user = User.objects.create(username ="johncena",password="123456john")
#
#         wallet = Wallet.objects.create(user = user, )

class TestWalletTransactionModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username = 'dineshkannuru' , first_name = 'dinesh' ,last_name = 'kannuru',
        email = 'dinesh@gmail.com',password = 'dinesh')
        wallet = Wallet.objects.create(user = user , credit = 100)
        transactions = Transaction.objects.create(wallet = wallet,initialcredit = 50,aftercredit=100,getcredit =50,
        organisation= 'Blood Bank' )

    def test_wallet(self):
        wallet = Wallet.objects.get(walletid = 1)
        self.assertEquals(wallet.credit,100)

    def test_transaction(self):
        transaction = Transaction.objects.get(transactionid = 1)
        self.assertEquals(transaction.initialcredit,50)
        self.assertEquals(transaction.aftercredit,100)
        self.assertEquals(transaction.getcredit,50)
        self.assertEquals(transaction.organisation,'Blood Bank')

from django.test.client import Client

class TestCreditView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='john',
        email='lennon@thebeatles.com', password='johnpassword')

    def test_insert(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('credits:insert'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credits/fail.html')


    def test_index(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('credits:index'))
        #self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/home/')
        #self.assertTemplateUsed(response, 'credits/index.html')


    def test_history(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('credits:history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credits/history.html')
