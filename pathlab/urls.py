from django.urls import path
from . import views

app_name = "pathlab"

urlpatterns = [
    path('', views.index,name='index'),
    path('result', views.result, name = "result"),
    path('booko', views.booko, name = "booko"),
    path('history', views.history, name = "history"),
    path('report/<int:rid>', views.report, name = "report"),
    path('api/', views.PathLabUser2class.as_view()),
]

