from django.db import models
from Maison.models import Maison
from location.models import Locataire
# Create your models here.
class Contrat(models.Model):
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Contrat de {self.locataire.nom} pour {self.maison.adresse}"
