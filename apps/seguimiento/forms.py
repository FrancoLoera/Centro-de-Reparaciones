from django import forms
from .models import EstatusOrdenDispositivo


class EstatusOrdenDispositivoForm(forms.ModelForm):
    class Meta:
        model = EstatusOrdenDispositivo
        fields = ["nombre"]
        labels = {"nombre": "Nombre"}
