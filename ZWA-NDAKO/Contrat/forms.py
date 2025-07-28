from django import forms
from .models import Contrat
from Maison.models import Maison
from location.models import Locataire
import datetime

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = ['maison', 'locataire', 'date_debut', 'date_fin']
        widgets = {
            'maison': forms.Select(attrs={'class': 'form-select'}),
            'locataire': forms.Select(attrs={'class': 'form-select'}),
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Vous pouvez filtrer les maisons ou locataires disponibles ici si besoin
        self.fields['maison'].queryset = Maison.objects.all()
        self.fields['locataire'].queryset = Locataire.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin:
            if date_fin <= date_debut:
                raise forms.ValidationError("La date de fin doit être postérieure à la date de début.")

            if date_debut < datetime.date.today():
                raise forms.ValidationError("La date de début ne peut pas être dans le passé.")

        return cleaned_data
