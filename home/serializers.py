from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    # address = UserAddressSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields='__all__'


class UserAddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    state = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = UserAddress
        fields = '__all__'

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        Detail, created = UserAddress.objects.update_or_create(user=user,
                                                               state=validated_data.pop('state'),
                                                               city=validated_data.pop('city'),
                                                               locality=validated_data.pop('locality'),
                                                               house=validated_data.pop('house'),
                                                               landmark=validated_data.pop('landmark'),
                                                               phone=validated_data.pop('phone'),
                                                               blood=validated_data.pop('blood'),
                                                               birth=validated_data.pop('birth'),
                                                               gender=validated_data.pop('gender'),
                                                               )

        return Detail


# class UserAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAddress
#         fields = ('state', 'city', 'locality', 'house', 'phone', 'birth', 'gender', 'blood')
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     address = UserAddressSerializer(required=True)
#     # password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'first_name', 'last_name', 'email', 'password', 'address')
#         extra_kwargs = {'password':{'write_only':True}}
#
#     def create(self, validated_data):
#         address_data = validated_data.pop('address')
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         UserAddress.objects.create(user=user, **address_data)
#         return user
#
#     def update(self, instance, validated_data):
#         address_data = validated_data.pop('address')
#         address = instance.address
#
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#
#         address.state = address_data.get('state', address.state)
#         address.city = address_data.get('city', address.city)
#         address.locality = address_data.get('locality', address.locality)
#         address.house = address_data.get('house', address.house)
#         address.phone = address_data.get('phone', address.phone)
#         address.birth = address_data.get('birth', address.birth)
#         address.gender = address_data.get('gender', address.gender)
#         address.blood = address_data.get('state', address.blood)
#
#         address.save()
#
#         return instance
