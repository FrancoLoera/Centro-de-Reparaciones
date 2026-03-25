from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from .models import EstatusOrdenDispositivo
from .forms import EstatusOrdenDispositivoForm


def estatus_list(request):
	estatuses = EstatusOrdenDispositivo.objects.all().order_by('nombre')
	return render(request, 'seguimiento/estatus_list.html', {'estatuses': estatuses})


def estatus_create(request):
	if request.method == 'POST':
		form = EstatusOrdenDispositivoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Estatus creado correctamente.')
			return redirect('seguimiento:estatus_list')
	else:
		form = EstatusOrdenDispositivoForm()
	return render(request, 'seguimiento/estatus_form.html', {'form': form, 'title': 'Crear estatus'})


def estatus_edit(request, pk):
	est = get_object_or_404(EstatusOrdenDispositivo, pk=pk)
	if request.method == 'POST':
		form = EstatusOrdenDispositivoForm(request.POST, instance=est)
		if form.is_valid():
			form.save()
			messages.success(request, 'Estatus actualizado.')
			return redirect('seguimiento:estatus_list')
	else:
		form = EstatusOrdenDispositivoForm(instance=est)
	return render(request, 'seguimiento/estatus_form.html', {'form': form, 'title': 'Editar estatus'})


def estatus_delete(request, pk):
	est = get_object_or_404(EstatusOrdenDispositivo, pk=pk)
	if request.method == 'POST':
		est.delete()
		messages.success(request, 'Estatus eliminado.')
		return redirect('seguimiento:estatus_list')
	return render(request, 'seguimiento/estatus_confirm_delete.html', {'estatus': est})
