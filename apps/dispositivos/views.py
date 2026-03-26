from django import forms
from django.shortcuts import get_object_or_404, redirect, render

from apps.core.forms import BootstrapModelForm
from apps.usuarios.utils import solo_tecnicos

from .models import Dispositivo, Marca
from apps.clientes.models import Cliente

class DispositivoForm(BootstrapModelForm):
    class Meta:
        model = Dispositivo
        fields = ["cliente", "alias", "numero_serie", "color", "marca"]
        labels = {
            "cliente": "idCliente",
            "alias": "alias",
            "numero_serie": "numeroSerie",
            "color": "color",
            "marca": "idMarca",
        }

    def clean(self):
        cleaned = super().clean()
        cliente = cleaned.get('cliente')
        if not cliente:
            raise forms.ValidationError('Debe seleccionar un cliente antes de crear el dispositivo.')
        return cleaned


class MarcaForm(BootstrapModelForm):
    class Meta:
        model = Marca
        fields = ["nombre"]
        labels = {"nombre": "nombre"}


@solo_tecnicos
def lista_dispositivos(request):
    dispositivos = Dispositivo.objects.select_related("marca").all()
    return render(
        request,
        "dispositivos/lista_dispositivos.html",
        {"dispositivos": dispositivos},
    )


@solo_tecnicos
def crear_dispositivo(request):
    if not Cliente.objects.exists():
        return redirect("clientes_crear")

    if request.method == "POST":
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispositivos_lista")
    else:
        form = DispositivoForm()

    return render(
        request,
        "dispositivos/form_dispositivo.html",
        {"form": form},
    )


@solo_tecnicos
def editar_dispositivo(request, pk):
    dispositivo = get_object_or_404(Dispositivo, pk=pk)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect("dispositivos_lista")
    else:
        form = DispositivoForm(instance=dispositivo)

    return render(
        request,
        "dispositivos/form_dispositivo.html",
        {"form": form, "dispositivo": dispositivo},
    )


@solo_tecnicos
def borrar_dispositivo(request, pk):
    dispositivo = get_object_or_404(Dispositivo, pk=pk)
    if request.method == "POST":
        dispositivo.delete()
        return redirect("dispositivos_lista")

    return render(
        request,
        "dispositivos/confirmar_borrar_dispositivo.html",
        {"dispositivo": dispositivo},
    )


@solo_tecnicos
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(
        request,
        "dispositivos/lista_marcas.html",
        {"marcas": marcas},
    )


@solo_tecnicos
def crear_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            # después de crear una marca, lo más útil es volver al formulario de dispositivo
            return redirect("dispositivos_crear")
    else:
        form = MarcaForm()

    return render(
        request,
        "dispositivos/form_marca.html",
        {"form": form},
    )


@solo_tecnicos
def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect("marcas_lista")
    else:
        form = MarcaForm(instance=marca)

    return render(
        request,
        "dispositivos/form_marca.html",
        {"form": form, "marca": marca},
    )


@solo_tecnicos
def borrar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        marca.delete()
        return redirect("marcas_lista")

    return render(
        request,
        "dispositivos/confirmar_borrar_marca.html",
        {"marca": marca},
    )
