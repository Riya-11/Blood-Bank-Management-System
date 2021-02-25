from rest_framework import serializers
from .models import *

class BloodAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = BloodAvailability
        fields = '__all__'
