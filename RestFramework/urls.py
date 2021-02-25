from django.urls import path, re_path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# from .views import UserViewSet
app_name = 'RestFramework'

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    re_path('^bloodstock/$', views.BloodAvailabilityList.as_view(), name='bloodstock'),
    re_path('^bloodstock/(?P<pk>[0-9]+)/$', views.BloodAvailabilityDetail.as_view(), name='bloodstock-detail'),
    re_path('^camps/$', views.BloodCampList.as_view(), name='camps'),
    re_path('^camps/(?P<pk>[0-9]+)/$', views.BloodCampDetail.as_view(), name='camp-detail'),
    re_path('^appointment/$', views.AppointmentList.as_view(), name='appointment'),
    re_path('^appointment/(?P<pk>[0-9]+)/$', views.AppointmentDetail.as_view(), name='appointment-detail'),
    re_path('^users/$', views.UserAddressList.as_view()),
    # re_path('^users/(?P<pk>[0-9]+)/$', views.UserAddressDetail.as_view(), name='user-detail'),
    re_path('^volunteers/$', views.BloodVolunteerList.as_view()),
    re_path('^volunteers/(?P<pk>[0-9]+)/$', views.BloodVolunteerDetail.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
