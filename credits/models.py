from django.db import models
from django.contrib.auth.models import User

# from home.models import Wallet,Transaction

organisation = (
    ('Blood Bank', 'Blood Bank'),
    ('Apollo Hospitals, Greams Road.', 'Apollo Hospitals, Greams Road.'),
    ('Chettinad Health City, Kelambakkam.', 'Chettinad Health City, Kelambakkam.'),
)


class Wallet(models.Model):
    walletid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    transactionid = models.AutoField(primary_key=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    initialcredit = models.IntegerField(blank=False)
    aftercredit = models.IntegerField(blank=False)
    getcredit = models.IntegerField(blank=False)
    organisation = models.CharField(max_length=40, choices=organisation)

    def updatewallet(self):
        self.wallet.credit = self.wallet.credit + self.getcredit

    def __str__(self):
        return self.wallet.user.username
