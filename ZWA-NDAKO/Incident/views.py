from django.shortcuts import render, get_object_or_404, redirect
from .models import Incident
from .forms import IncidentForm
from django.contrib import messages

def incident_list(request):
    incidents = Incident.objects.select_related('maison').all()
    return render(request, 'incident/incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'incident/incident_detail.html', {'incident': incident})

def incident_create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Incident signalé avec succès.")
            return redirect('incident:incident_list')
    else:
        form = IncidentForm()
    return render(request, 'incident/incident_form.html', {'form': form, 'title': 'Signaler un incident'})

def incident_update(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            messages.success(request, "Incident mis à jour avec succès.")
            return redirect('incident:incident_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incident/incident_form.html', {'form': form, 'title': 'Modifier un incident'})

def incident_delete(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        incident.delete()
        messages.success(request, "Incident supprimé.")
        return redirect('incident:incident_list')
    return render(request, 'incident/incident_confirm_delete.html', {'incident': incident})
