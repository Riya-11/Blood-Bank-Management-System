from django.db import models
from django import forms
from django.contrib.auth.models import User
from home.models import *

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

Test_Type = (
    ('Regular Checkup1', 'Regular Checkup1'),
    ('Regular Checkup2', 'Regular Checkup2'),
    ('Regular Checkup3', 'Regular Checkup3'),
)

'''class PathLabUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pathlab = models.ForeignKey(PathLabs, on_delete=models.CASCADE)
    testtype = models.CharField(blank=False, max_length=1000)
    feedback = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return self.user
'''

class PathLabUser2(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    firstname = models.CharField(null=False, max_length=1000)
    lastname = models.CharField(null=True, max_length=1000)
    address = models.CharField(null=False, max_length=1000)
    bloodgroup = models.CharField(null=False, choices=Blood_Groups, max_length=3)
    testtype = models.CharField(null=False, max_length=1000, choices=Test_Type)
    date = models.DateTimeField(auto_now_add=True)
    Result = models.CharField(null=False, max_length=1000, default='NA')
    feedback = models.CharField(null=False, max_length=1000, default='NA')

    def __str__(self):
        return self.firstname
