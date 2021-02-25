from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'stock'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^mail', views.sendingmail, name='sendingmail')

]
