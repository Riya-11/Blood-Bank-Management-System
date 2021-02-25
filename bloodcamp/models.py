from django.db import models
from datetime import date

# Create your models here.


Blood_Groups = (
    ('A+', 'A-'),
    ('A-', 'A+'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
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


class BloodCamp(models.Model):
    # campid = models.CharField(blank=False, null=False, max_length=150)
    campid = models.AutoField(primary_key=True)
    startdate = models.DateField(default=date.today)
    enddate = models.DateField(default=date.today)
    location = models.CharField(blank=False, null=False, max_length=150)
    status = models.CharField(default='1', max_length=1)

    def __str__(self):
        return str(self.campid) + " " + self.location


    def checkingbloodcamp(self):
        return self.location

class BloodCampDonor(models.Model):
    firstname = models.CharField(blank=False, null=False, max_length=150)
    lastname = models.CharField(blank=False, null=False, max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=11, blank=True)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateField(auto_now=True, auto_now_add=False)
    blood = models.CharField(max_length=10, choices=Blood_Groups, default='B-')
    bloodcamp = models.ForeignKey(BloodCamp, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def checkingdonor(self):
        return '%s, %s, %s, %s' % (self.firstname,
        self.email, self.phone, self.bloodcamp)


class BloodVolunteer(models.Model):
    name = models.CharField(blank=False, max_length=100)
    nickname = models.CharField(blank=False, max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, blank=False)
    state = models.CharField(max_length=30, choices=States, default='Andhra Pradesh')
    city = models.CharField(blank=False, null=False, max_length=200, default='Agra')
    locality = models.CharField(blank=False, max_length=400)
    house = models.CharField(blank=False, max_length=200)
    landmark = models.CharField(blank=False, max_length=200)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now_add=True)
    blood = models.CharField(max_length=10, choices=Blood_Groups)
    bloodcamp = models.ForeignKey(BloodCamp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def checkingvolunteer(self):
        return '%s, %s, %s, %s' % (self.name,
        self.email, self.phone, self.bloodcamp)