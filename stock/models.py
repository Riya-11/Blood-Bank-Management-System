from django.db import models
from home.models import *


# Create your models here.
class BloodAvailability(models.Model):
    threshhold = models.IntegerField(default=0)
    bloodgroup_A_plus = models.IntegerField(default=0)
    bloodgroup_A_minus = models.IntegerField(default=0)
    bloodgroup_B_plus = models.IntegerField(default=0)
    bloodgroup_B_minus = models.IntegerField(default=0)
    bloodgroup_O_plus = models.IntegerField(default=0)
    bloodgroup_O_minus = models.IntegerField(default=0)
    bloodgroup_AB_plus = models.IntegerField(default=0)
    bloodgroup_AB_minus = models.IntegerField(default=0)
