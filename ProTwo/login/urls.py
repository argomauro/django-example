from django.urls import path, re_path
from django.conf.urls import url
from login import views

app_name='login'

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register'),
    path('logout',views.user_logout, name='logout'),
    path('special',views.special, name='special'),
    path('login',views.user_login, name='user_login'),


]
