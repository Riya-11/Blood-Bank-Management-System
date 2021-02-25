from django.urls import path,re_path
from . import views

app_name = 'requestblood'

urlpatterns = [
    path('',views.redi,name='red'),
    path('<req_blood>/', views.index, name='index'),
    re_path(r'^sorry/$', views.sorry, name='sorry'),
    re_path(r'^response/$', views.response, name='response'),
]
