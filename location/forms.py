from django import forms
from .models import Maison, Locataire, Contrat, Paiement, Incident




class MaisonForm(forms.ModelForm):
    class Meta:
        model = Maison
        fields = '__all__'

class LocataireForm(forms.ModelForm):
    class Meta:
        model = Locataire
        fields = '__all__'

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = '__all__'

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'
