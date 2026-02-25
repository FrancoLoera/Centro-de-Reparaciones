from django import forms
from django.shortcuts import get_object_or_404, redirect, render

from .models import Dispositivo, Marca


class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ["alias", "numero_serie", "color", "marca"]


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nombre"]


def lista_dispositivos(request):
    dispositivos = Dispositivo.objects.select_related("marca").all()
    return render(
        request,
        "dispositivos/lista_dispositivos.html",
        {"dispositivos": dispositivos},
    )


def crear_dispositivo(request):
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


def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(
        request,
        "dispositivos/lista_marcas.html",
        {"marcas": marcas},
    )


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
