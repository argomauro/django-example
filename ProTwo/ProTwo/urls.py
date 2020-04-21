from django.contrib import admin
from django.urls import path, include
from AppTwo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appTwo/', include('AppTwo.urls')),
    path('auth/', include('login.urls')),
    path('', views.index),

]
