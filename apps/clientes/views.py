from django import forms
from django.shortcuts import redirect, render

from apps.core.forms import BootstrapModelForm
from apps.usuarios.utils import solo_tecnicos

from .models import Cliente


class ClienteForm(BootstrapModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre_completo", "telefono", "telefono_alternativo", "email"]
        labels = {
            "nombre_completo": "nombreCompleto",
            "telefono": "telefono",
            "telefono_alternativo": "telefonoAlternativo",
            "email": "email",
        }


@solo_tecnicos
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by("-id_cliente")
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})


@solo_tecnicos
def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes_lista")
    else:
        form = ClienteForm()

    return render(request, "clientes/form_cliente.html", {"form": form})
