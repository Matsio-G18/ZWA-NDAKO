from django.contrib import admin
from .models import Maison

@admin.register(Maison)
class MaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'adresse', 'loyer', 'statut')
    list_filter = ('statut',)
    search_fields = ('adresse', 'description')
