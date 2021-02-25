from rest_framework.permissions import SAFE_METHODS
from availability.serializers import BloodAvailabilitySerializer
from availability.models import *
from home.models import *
from home.serializers import *
from bloodcamp.models import *
from bloodcamp.serializers import *
from donate.serializers import *
from donate.models import Appointment
from rest_framework import generics, permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class BloodAvailabilityList(generics.ListCreateAPIView):
    queryset = BloodAvailability.objects.all()
    serializer_class = BloodAvailabilitySerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class BloodAvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodAvailability.objects.all()
    serializer_class = BloodAvailabilitySerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class UserAddressList(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


# class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserAddress.objects.all()
#     serializer_class = UserAddressSerializer
#     permission_classes = (IsAdminUserOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class BloodCampList(generics.ListCreateAPIView):
    queryset = BloodCamp.objects.all()
    serializer_class = BloodCampSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class BloodCampDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodCamp.objects.all()
    serializer_class = BloodCampSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class BloodVolunteerList(generics.ListCreateAPIView):
    queryset = BloodVolunteer.objects.all()
    serializer_class = BloodVolunteerSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class BloodVolunteerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodVolunteer.objects.all()
    serializer_class = BloodVolunteerSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
