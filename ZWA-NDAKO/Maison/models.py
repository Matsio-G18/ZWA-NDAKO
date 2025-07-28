from django.db import models

# Create your models here.
class Maison(models.Model):
    adresse =  models.TextField()
    description = models.TextField()
    loyer = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=15, choices=[('libre', 'Libre'), ('occupé', 'Occupé')])

    def __str__(self):
        return self.adresse