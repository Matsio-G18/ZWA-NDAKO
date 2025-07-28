from django.urls import path
from . import views

app_name = 'maison'

urlpatterns = [
    path('', views.maison_list, name='maison_list'),
    path('ajouter/', views.maison_create, name='maison_create'),
    path('modifier/<int:pk>/', views.maison_update, name='maison_update'),
    path('supprimer/<int:pk>/', views.maison_delete, name='maison_delete'),
]
