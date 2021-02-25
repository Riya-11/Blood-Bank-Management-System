from django.urls import path, re_path
from . import views

app_name = 'finddonor'

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
