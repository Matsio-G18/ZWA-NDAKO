from django import forms
from .models import Incident
from Maison.models import Maison

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['maison', 'description', 'statut']
        widgets = {
            'maison': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['maison'].queryset = Maison.objects.all()

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description or len(description.strip()) < 10:
            raise forms.ValidationError("La description doit contenir au moins 10 caractères.")
        return description

    def clean_statut(self):
        statut = self.cleaned_data.get('statut')
        if statut not in dict(Incident._meta.get_field('statut').choices):
            raise forms.ValidationError("Statut invalide.")
        return statut
