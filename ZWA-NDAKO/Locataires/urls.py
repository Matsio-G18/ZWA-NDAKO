from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('', views.locataire_list, name='locataire_list'),
    path('nouveau/', views.locataire_create, name='locataire_create'),
    path('modifier/<int:pk>/', views.locataire_update, name='locataire_update'),
    path('supprimer/<int:pk>/', views.locataire_delete, name='locataire_delete'),
    path('rechercher/', views.locataire_search, name='locataire_search'),
]
