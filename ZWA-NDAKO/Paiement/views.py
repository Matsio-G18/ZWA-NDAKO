from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paiement
from .forms import PaiementForm  # à créer dans forms.py

# Liste des paiements
def paiement_list(request):
    paiements = Paiement.objects.all()
    return render(request, 'paiement/paiement_list.html', {'paiements': paiements})

# Création d’un paiement
def paiement_create(request):
    if request.method == 'POST':
        form = PaiementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paiement:paiement_list')
    else:
        form = PaiementForm()
    return render(request, 'paiement/paiement_form.html', {'form': form})

# Modification d’un paiement
def paiement_update(request, pk):
    paiement = get_object_or_404(Paiement, pk=pk)
    if request.method == 'POST':
        form = PaiementForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()
            return redirect('paiement:paiement_list')
    else:
        form = PaiementForm(instance=paiement)
    return render(request, 'paiement/paiement_form.html', {'form': form})

# Suppression d’un paiement
def paiement_delete(request, pk):
    paiement = get_object_or_404(Paiement, pk=pk)
    if request.method == 'POST':
        paiement.delete()
        return redirect('paiement:paiement_list')
    return render(request, 'paiement/paiement_confirm_delete.html', {'paiement': paiement})
