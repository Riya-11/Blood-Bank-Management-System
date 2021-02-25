from django.urls import path,re_path
from . import views

app_name = 'credits'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('insert/',views.insert,name = 'insert'),
    path('history/',views.history,name = 'history')
]
