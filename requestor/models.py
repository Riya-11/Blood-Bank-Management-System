from django.db import models

# Create your models here.
from django import forms
from django.contrib.auth.models import User
import datetime
from home.models import State, City
from django.core.validators import RegexValidator




class New_requestor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rig = models.CharField(max_length=30)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    locality = models.CharField(max_length=400)
    landmark = models.CharField(null= True, max_length=200, blank=True)
    phone = models.CharField(max_length=10,
                             validators=[
                                 RegexValidator(
                                     regex='^[1-9]{1}[0-9]{9}$',
                                     message='Enter a valid phone no',
                                     code='invalid_cell'
                                 ),
                             ]

                             )

    def __str__(self):
        return self.user.username
