from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su correo electrónico"
        })
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su contraseña"
        })
    )

    error_messages = {
        "invalid_login": "Usuario o contraseña incorrectos",
        "inactive": "Esta cuenta está desactivada",
    }