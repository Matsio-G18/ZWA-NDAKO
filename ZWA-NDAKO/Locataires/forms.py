from django import forms
from .models import Locataire

class LocataireForm(forms.ModelForm):
    class Meta:
        model = Locataire
        fields = ['nom', 'email', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemple@mail.com'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
        }

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom or len(nom.strip()) < 2:
            raise forms.ValidationError("Le nom doit contenir au moins 2 caractères.")
        return nom.strip()

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if telephone and not telephone.isdigit():
            raise forms.ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")
        return telephone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Locataire.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé par un autre locataire.")
        return email
