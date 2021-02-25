from django.urls import path, re_path
from . import views

app_name = 'bloodcamp'

urlpatterns = [
    path('volunteering/', views.Volunteering, name="volunteering"),
    path('volunteerlist/', views.VolunteerList, name="volunteer_list"),
    path('history/', views.history, name='history'),
    path('', views.camphome, name='camphome'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('ongoing/', views.ongoing, name='ongoing'),
    path('newdonor/', views.newdonorpage, name='newdonorpage'),
    path('newcamp/', views.newcamppage, name='newcamppage'),

]
