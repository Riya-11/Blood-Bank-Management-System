from django.urls import path, include
from . import views


app_name = 'donate'
urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/',views.thanks, name='thanks'),
]
