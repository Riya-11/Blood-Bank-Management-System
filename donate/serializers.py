from rest_framework import serializers
from .models import *
from . import ref

class UserSerializer(serializers.ModelSerializer):
    # address = UserAddressSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class AppointmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        refno = ref.generate_app_id()
        Detail, created = Appointment.objects.update_or_create(user=user,
                                                               date=validated_data.pop('date'),
                                                               time=validated_data.pop('time'),
                                                               pathlab=validated_data.pop('pathlab'),
                                                               reference_no=refno,

                                                               )

        return Detail
