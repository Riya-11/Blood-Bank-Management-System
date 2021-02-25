from django.urls import path,re_path
from . import views

app_name = 'display'

urlpatterns = [
    path('',views.index,name = 'index')
]
