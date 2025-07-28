from django import forms
from .models import Paiement
from Contrat.models import Contrat
import datetime

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['contrat', 'date', 'montant']
        widgets = {
            'contrat': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant en euros'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contrat'].queryset = Contrat.objects.all()

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date > datetime.date.today():
            raise forms.ValidationError("La date de paiement ne peut pas être dans le futur.")
        return date

    def clean_montant(self):
        montant = self.cleaned_data.get('montant')
        if montant is None or montant <= 0:
            raise forms.ValidationError("Le montant doit être un nombre positif.")
        return montant
