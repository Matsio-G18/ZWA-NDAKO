from django.contrib import admin
from .models import Locataire

@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email', 'telephone')
    search_fields = ('nom', 'email', 'telephone')
