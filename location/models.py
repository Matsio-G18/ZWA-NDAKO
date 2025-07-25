from django.db import models

# Create your models here.

class Maison(models.Model):
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    loyer = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=50, choices=[('libre', 'Libre'), ('occupé', 'Occupé')])

    def __str__(self):
        return self.adresse



    
class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom

class Contrat(models.Model):
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Contrat de {self.locataire.nom} pour {self.maison.adresse}"

class Paiement(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.montant}€"

class Incident(models.Model):
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    description = models.TextField()
    date_signalement = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=[('en attente', 'En attente'), ('résolu', 'Résolu')])

    def __str__(self):
        return f"Incident {self.maison.adresse} - {self.statut}"
    