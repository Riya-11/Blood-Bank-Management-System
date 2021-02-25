from django.db import models
from home.models import UserAddress
from django.contrib.auth.models import User


# Create your models here.

Path_labs = (
    ('Chennai', 'Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Patna', 'Patna'),
    ('Mumbai', 'Mumbai'),
    ('Hyderabad', 'Hyderabad'),
    ('Kolkata', 'Kolkata'),
    ('Delhi', 'Delhi'),
    ('Jamshedpur', 'Jamshedpur'),
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    reference_no = models.CharField(blank=False, null=False, max_length=200)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    pathlab = models.CharField(max_length=30, choices=Path_labs, default='Chennai')


    def __str__(self):
        return self.reference_no

    def checkingappointment(self):
        return '%s, %s' % (self.user.username, self.reference_no)


