from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from home.models import State,City
# Create your models here.

Blood_Groups = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

States = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('karnataka', 'karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Goa', 'Goa'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),

)

class Requestor(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    blood = models.CharField(max_length=10, choices=Blood_Groups, blank=False,editable=False)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    phone = models.CharField(blank=False, null=False, max_length=10,
                             validators=[
                                 RegexValidator(
                                     regex='^[1-9]{1}[0-9]{9}$',
                                     message='Enter a valid phone no',
                                     code='invalid_cell'
                                 ),
                             ]
                             )
    email = models.EmailField(blank=False, null=False, max_length=254)
    reason = models.CharField(blank=False, null=False, max_length=500)
    date = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.name + " " + self.reason

    def checkingrequestor(self):
        return '%s, %s, %s, %s' % (self.name, self.phone, self.email, self.reason)

