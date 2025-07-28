from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Maison
from .forms import MaisonForm  # Ce formulaire doit être créé (voir plus bas)

# Lister les maisons
def maison_list(request):
    maisons = Maison.objects.all()
    return render(request, 'maison/maison_list.html', {'maisons': maisons})

# Créer une maison
def maison_create(request):
    if request.method == 'POST':
        form = MaisonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maison:maison_list')
    else:
        form = MaisonForm()
    return render(request, 'maison/maison_form.html', {'form': form})

# Modifier une maison
def maison_update(request, pk):
    maison = get_object_or_404(Maison, pk=pk)
    if request.method == 'POST':
        form = MaisonForm(request.POST, instance=maison)
        if form.is_valid():
            form.save()
            return redirect('maison:maison_list')
    else:
        form = MaisonForm(instance=maison)
    return render(request, 'maison/maison_form.html', {'form': form})

# Supprimer une maison
def maison_delete(request, pk):
    maison = get_object_or_404(Maison, pk=pk)
    if request.method == 'POST':
        maison.delete()
        return redirect('maison:maison_list')
    return render(request, 'maison/maison_confirm_delete.html', {'maison': maison})
