from django.urls import path, re_path
from django.conf.urls import url
from AppTwo import views
app_name='AppTwo'
urlpatterns = [
    path('', views.index_user),
    path('<str:utente_nome>/', views.detailUtente, name='detailUtente'),
    path('conti', views.index_conticorrente),
    path('form',views.utente_form, name='formUtente'),
    path('other',views.other),
    re_path(r'^help', views.help)
]
