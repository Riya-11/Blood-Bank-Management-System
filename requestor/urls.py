from django.contrib import admin
from django.urls import path, re_path
from . import views
# from django.contrib.auth.views import logout_views
from django.contrib.auth import views as auth_views

app_name = 'requestor'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/',views.requestor_Login, name="requestor_Login"),
    path('logout/',views.requestor_logout,name="requestor_logout"),
    path('profile/', views.profile, name="profile"),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]
