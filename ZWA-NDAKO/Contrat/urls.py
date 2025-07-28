from django.urls import path
from . import views

app_name = 'contrat'

urlpatterns = [
    path('', views.contrat_list, name='contrat_list'),                    # Liste des contrats
    path('nouveau/', views.contrat_create, name='contrat_create'),        # Créer un contrat
    path('modifier/<int:pk>/', views.contrat_update, name='contrat_update'),  # Modifier un contrat
    path('supprimer/<int:pk>/', views.contrat_delete, name='contrat_delete'),  # Supprimer un contrat
    path('<int:pk>/', views.contrat_detail, name='contrat_detail'),       # Détail d'un contrat
]
