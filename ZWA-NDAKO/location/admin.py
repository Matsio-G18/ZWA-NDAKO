from django.contrib import admin
from .models import Maison, Locataire, Contrat, Paiement, Incident
from django.contrib.admin.sites import AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib.staticfiles.storage import staticfiles_storage
#Enregistrer les models ici 

class MaisonAdmin(admin.ModelAdmin):
    list_display = ('adresse', 'loyer', 'statut')
    list_filter = ('statut',)
    search_fields = ('adresse',)
    ordering = ('adresse',)

class LocataireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone')
    search_fields = ('nom', 'email')

class ContratAdmin(admin.ModelAdmin):
    list_display = ('maison', 'locataire', 'date_debut', 'date_fin')
    list_filter = ('date_debut', 'date_fin')
    search_fields = ('maison__adresse', 'locataire__nom')

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('contrat', 'date', 'montant')
    list_filter = ('date',)
    search_fields = ('contrat__maison__adresse',)

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('maison', 'statut', 'date_signalement')
    list_filter = ('statut',)
    search_fields = ('maison__adresse', 'description')
    readonly_fields = ('date_signalement',)
    list_display_links = ('maison',)
    actions = ['mark_as_resolved']
    
    

    def mark_as_resolved(self, request, queryset):
        updated = queryset.update(statut='Résolu')
        self.message_user(request, f"{updated} incident(s) mis à jour en 'Résolu'.")
    mark_as_resolved.short_description = "Marquer les incidents sélectionnés comme Résolu"


class CustomAdminSite(admin.AdminSite):
    site_header = "🛠️ Gesloc - Administration"
    site_title = "Gesloc Admin"
    index_title = "Tableau de bord Gesloc"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = staticfiles_storage.url('css/admin.css')
        return context

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        context = dict(
            self.each_context(request),
            maisons_count=Maison.objects.count(),
            locataires_count=Locataire.objects.count(),
            incidents_ouverts=Incident.objects.filter(statut='Ouvert').count(),
            incidents_resolus=Incident.objects.filter(statut='Résolu').count()
        )
        return render(request, "admin/admin_dashboard.html", context)

# Ensuite, utilise ce custom admin :
custom_admin = CustomAdminSite(name='custom_admin')
custom_admin.register(Maison, MaisonAdmin)
custom_admin.register(Locataire, LocataireAdmin)
custom_admin.register(Contrat, ContratAdmin)
custom_admin.register(Paiement, PaiementAdmin)
custom_admin.register(Incident, IncidentAdmin)

# Et dans ton fichier templates/admin/base_site.html (voir ci-dessous)

admin.site.site_header = "Gestion des Maisons en Location"
admin.site.site_title = "Administration ZWA NDAKO"
admin.site.index_title = "Bienvenue sur le tableau d\'administration ZWA NDAKO "
admin.site.register(Maison, MaisonAdmin)
admin.site.register(Locataire, LocataireAdmin)
admin.site.register(Contrat, ContratAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(Incident, IncidentAdmin)
