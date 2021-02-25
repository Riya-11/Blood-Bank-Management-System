from django.urls import path, include
from . import views
from django.urls import reverse_lazy

app_name = "Hospitals"

urlpatterns = [
    path('', views.hospitals,name="hospitals"),
]
