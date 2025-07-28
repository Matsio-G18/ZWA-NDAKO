from django.urls import path
from . import views

app_name = 'paiement'

urlpatterns = [
    path('', views.paiement_list, name='paiement_list'),
    path('ajouter/', views.paiement_create, name='paiement_create'),
    path('modifier/<int:pk>/', views.paiement_update, name='paiement_update'),
    path('supprimer/<int:pk>/', views.paiement_delete, name='paiement_delete'),
]
