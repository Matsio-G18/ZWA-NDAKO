from django.db import models
from Maison.models import Maison
# Create your models here.
class Incident(models.Model):
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    description = models.TextField()
    date_signalement = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=15, choices=[('en attente', 'En attente'), ('résolu', 'Résolu')])

    def __str__(self):
        return f"Incident {self.maison.adresse} - {self.statut}"
    