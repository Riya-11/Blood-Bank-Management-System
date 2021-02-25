from django.core.validators import RegexValidator
from django.db import models
from django import forms
from django.contrib.auth.models import User
import datetime

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

organisation = (
    ('Blood Bank', 'Blood Bank'),
    ('Apollo Hospitals, Greams Road.', 'Apollo Hospitals, Greams Road.'),
    ('Chettinad Health City, Kelambakkam.', 'Chettinad Health City, Kelambakkam.'),
)

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

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender'),
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


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def checkingstate(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def checkingcity(self):
        return '%s, %s' % (self.name, self.state.name)



class UserAddress(models.Model):
    useraddressid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, max_length=200)
    locality = models.CharField(max_length=400)
    house = models.CharField(max_length=200)
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
    birth = models.DateField(null = False)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now_add=True)
    blood = models.CharField(max_length=10, choices=Blood_Groups)

    # last_donated = models.ForeignKey(UserHistory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

    def checkinguser(self):
        return '%s, %s, %s' % (self.user.username, self.user.email, self.phone)
        #self.user.first_name, self.user.last_name, self.birth, self.phone,
        #self.gender, self.date, self.blood,self.state.name, self.city.name)



class UserProfile(models.Model):
    userprofileid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # donoraddress = models.OneToOneField(DonorAddress,on_delete = models.CASCADE)
    status = models.CharField(blank=True, max_length=200)
    feedback = models.CharField(blank=True, max_length=1000)
    image = models.ImageField(upload_to="profile_image", blank=True)

    def __str__(self):
        return self.user.username

    def checkinguserprofile(self):
        return '%s, %s' % (self.user.username, self.status)


class UserHistory(models.Model):
    userhistoryid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username
