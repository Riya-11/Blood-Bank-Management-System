from django.contrib import admin
from django.urls import path, re_path
from . import views
# from django.contrib.auth.views import logout_views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.SignUp, name="signup"),
    path('login/', views.LogIn, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    path('upload/', views.Image_Upload, name="image_upload"),
    path('update_details/', views.Update_Details, name="update_details"),
    path('update_password/', views.Update_Password, name="update_password"),
    path('faq/', views.faq, name="faq"),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    path('readmore/',views.readmore,name="readmore"),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name="password_reset"),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    re_path(r'^password_reset/complete/$', auth_views.PasswordResetCompleteView.as_view(),
            name="password_reset_complete"),
    re_path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),

]
