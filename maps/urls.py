from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('bloodbanks/',views.index,name = 'index'),
    path('pathlab/',views.index1,name = 'pathlab')
]
