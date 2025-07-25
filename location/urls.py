from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('maisons/', views.liste_maisons, name='liste_maisons'),
    path('locataires/', views.liste_locataires, name='liste_locataires'),
    path('paiements/', views.liste_paiements, name='liste_paiements'),
    path('contrats/', views.liste_contrats, name='liste_contrats'),
    path('incidents/', views.liste_incidents, name='liste_incidents'),
    path('ajouter_maison/', views.ajouter_maison, name='ajouter_maison'),
    
]
 