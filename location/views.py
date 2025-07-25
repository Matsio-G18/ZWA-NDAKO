from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Maison, Locataire, Paiement, Contrat, Incident
from .forms import MaisonForm
# Create your views here.

def home(request):
    maisons = Maison.objects.all()
    context = {
        'maisons': maisons,
        'maisons_count': maisons.count(),
        'locataires_count': Locataire.objects.count(),
        'contrats_count': Contrat.objects.count(),
        'paiements_count': Paiement.objects.count(),
    }
    return render(request, 'location/home.html', context)


def ajouter_maison(request):
    if request.method == 'POST':
        maison_form = MaisonForm(request.POST)
        
        if maison_form.is_valid() :
            maison = maison_form.save()
        
    else:
        maison_form = MaisonForm()

    return render(request, 'location/ajouter_maison.html', {
        'maison_form': maison_form,
    })


def liste_maisons(request):
    maisons = Maison.objects.all()
    return render(request, 'location/maisons.html', {'maisons': maisons})

def liste_locataires(request):
    locataires = Locataire.objects.all()
    return render(request, 'location/locataires.html', {'locataires': locataires})

def liste_paiements(request):
    paiements = Paiement.objects.all()
    return render(request, 'location/paiements.html', {'paiements': paiements})

def liste_contrats(request):
    contrats = Contrat.objects.all()
    return render(request, 'location/contrats.html', {'contrats': contrats})

def liste_incidents(request):
    incidents = Incident.objects.all()
    return render(request, 'location/incidents.html', {'incidents': incidents})
