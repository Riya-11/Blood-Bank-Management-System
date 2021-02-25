from django.db import models

class BloodBankName(models.Model):
    bloodbankid = models.AutoField(primary_key=True)
    bloodbankname = models.CharField(max_length=30)
    latitude = models.FloatField(max_length=30)
    longitude = models.FloatField(max_length=30)
    
    def __str__(self):
        return self.bloodbankname
        
class PathlabName(models.Model):
    pathlabid = models.AutoField(primary_key=True)
    pathlabname = models.CharField(max_length=30)
    latitude = models.FloatField(max_length=30)
    longitude = models.FloatField(max_length=30)
    
    def __str__(self):
        return self.pathlabname
