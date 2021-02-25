from django.db import models

class Hospital(models.Model):
    Hospitalid = models.AutoField(primary_key=True)
    Hospital_name = models.CharField(max_length=100)
    Hospital_address = models.CharField(max_length=1000)
    
