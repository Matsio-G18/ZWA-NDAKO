from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrat', 'date', 'montant')
    list_filter = ('date',)
    search_fields = ('contrat__maison__adresse', 'contrat__locataire__nom')
