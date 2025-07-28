from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'maison', 'description', 'date_signalement', 'statut')
    list_filter = ('statut', 'date_signalement')
    search_fields = ('maison__adresse', 'description')
