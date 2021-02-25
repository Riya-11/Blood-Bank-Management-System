from rest_framework import serializers
from .models import *


class BloodCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodCamp
        fields = ('campid', 'startdate', 'enddate', 'location')


class BloodVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodVolunteer
        fields = ('name', 'blood', 'bloodcamp', 'city')
