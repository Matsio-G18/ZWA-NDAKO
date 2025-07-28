from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contrat

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ('id', 'maison', 'locataire', 'date_debut', 'date_fin')
    list_filter = ('date_debut', 'date_fin', 'maison', 'locataire')
    search_fields = ('maison__adresse', 'locataire__nom')
