from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contrat
from .forms import ContratForm
from django.contrib import messages

# Liste des contrats
def contrat_list(request):
    contrats = Contrat.objects.select_related('maison', 'locataire').all()
    return render(request, 'contrat/contrat_list.html', {'contrats': contrats})

# Détail d’un contrat
def contrat_detail(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    return render(request, 'contrat/contrat_detail.html', {'contrat': contrat})

# Créer un nouveau contrat
def contrat_create(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contrat enregistré avec succès.")
            return redirect('contrat:contrat_list')
    else:
        form = ContratForm()
    return render(request, 'contrat/contrat_form.html', {'form': form, 'title': 'Nouveau Contrat'})

# Modifier un contrat
def contrat_update(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    if request.method == 'POST':
        form = ContratForm(request.POST, instance=contrat)
        if form.is_valid():
            form.save()
            messages.success(request, "Contrat modifié avec succès.")
            return redirect('contrat:contrat_list')
    else:
        form = ContratForm(instance=contrat)
    return render(request, 'contrat/contrat_form.html', {'form': form, 'title': 'Modifier Contrat'})

# Supprimer un contrat
def contrat_delete(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    if request.method == 'POST':
        contrat.delete()
        messages.success(request, "Contrat supprimé avec succès.")
        return redirect('contrat:contrat_list')
    return render(request, 'contrat/contrat_confirm_delete.html', {'contrat': contrat})
