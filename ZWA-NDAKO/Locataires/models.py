from django.db import models

# Create your models here.
class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    telephone = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nom
