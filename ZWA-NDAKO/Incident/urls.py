from django.urls import path
from . import views

app_name = 'incident'

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('<int:pk>/', views.incident_detail, name='incident_detail'),
    path('ajouter/', views.incident_create, name='incident_create'),
    path('<int:pk>/modifier/', views.incident_update, name='incident_update'),
    path('<int:pk>/supprimer/', views.incident_delete, name='incident_delete'),
]
