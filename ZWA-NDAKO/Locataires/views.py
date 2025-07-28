from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Locataire
from .forms import LocataireForm

def locataire_list(request):
    locataires = Locataire.objects.all()
    return render(request, 'location/locataire_list.html', {'locataires': locataires})

def locataire_create(request):
    if request.method == 'POST':
        form = LocataireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location:locataire_list')
    else:
        form = LocataireForm()
    return render(request, 'location/locataire_form.html', {'form': form})

def locataire_update(request, pk):
    locataire = get_object_or_404(Locataire, pk=pk)
    if request.method == 'POST':
        form = LocataireForm(request.POST, instance=locataire)
        if form.is_valid():
            form.save()
            return redirect('location:locataire_list')
    else:
        form = LocataireForm(instance=locataire)
    return render(request, 'location/locataire_form.html', {'form': form})

def locataire_delete(request, pk):
    locataire = get_object_or_404(Locataire, pk=pk)
    if request.method == 'POST':
        locataire.delete()
        return redirect('location:locataire_list')
    return render(request, 'location/locataire_confirm_delete.html', {'locataire': locataire})

def locataire_search(request):
    query = request.GET.get('q')
    locataires = Locataire.objects.filter(nom__icontains=query) if query else Locataire.objects.all()
    return render(request, 'location/locataire_list.html', {'locataires': locataires})
