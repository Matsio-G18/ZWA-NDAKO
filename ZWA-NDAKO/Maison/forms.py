from django import forms
from .models import Maison

class MaisonForm(forms.ModelForm):
    class Meta:
        model = Maison
        fields = ['adresse', 'description', 'loyer', 'statut']
        widgets = {
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description de la maison'}),
            'loyer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant du loyer'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_adresse(self):
        adresse = self.cleaned_data.get('adresse')
        if not adresse or len(adresse.strip()) < 5:
            raise forms.ValidationError("L’adresse doit contenir au moins 5 caractères.")
        return adresse.strip()

    def clean_loyer(self):
        loyer = self.cleaned_data.get('loyer')
        if loyer is None or loyer <= 0:
            raise forms.ValidationError("Le loyer doit être un montant positif.")
        return loyer

    def clean_statut(self):
        statut = self.cleaned_data.get('statut')
        if statut not in dict(Maison._meta.get_field('statut').choices):
            raise forms.ValidationError("Statut invalide.")
        return statut
