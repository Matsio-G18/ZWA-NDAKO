from django.db import models
from Contrat.models import Contrat
# Create your models here.
class Paiement(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.montant}€"