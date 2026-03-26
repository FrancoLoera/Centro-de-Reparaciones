from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from .utils import es_tecnico, solo_tecnicos, solo_staff
from apps.ordenes.models import Orden
from apps.seguimiento.models import EstatusOrdenDispositivo
from .models import Tecnico


class LoginTecnicoForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.setdefault("class", "form-control")
        self.fields["password"].widget.attrs.setdefault("class", "form-control")


def portal_publico(request):
    """
    Entrada publica: sin listados ni datos de negocio.
    Visitante (cliente potencial) no ve el panel; solo mensaje y acceso a login de tecnicos.
    """
    if request.user.is_authenticated:
        if es_tecnico(request.user):
            return redirect("dashboard_tecnico")
        if request.user.is_staff or request.user.is_superuser:
            return redirect("admin:index")
        return _sin_perfil_tecnico(request)
    return render(request, "usuarios/portal_publico.html")


def _sin_perfil_tecnico(request):
    from django.shortcuts import render

    return render(
        request,
        "usuarios/sin_acceso_tecnico.html",
        {"es_staff": request.user.is_staff},
        status=403,
    )


class LoginTecnicoView(LoginView):
    template_name = "usuarios/login_tecnico.html"
    authentication_form = LoginTecnicoForm
    redirect_authenticated_user = True


class LogoutTecnicoView(LogoutView):
    next_page = "/"


@solo_tecnicos
def dashboard_tecnico(request):
    ordenes_recientes = Orden.objects.select_related("cliente", "dispositivo", "estatus").order_by("-id_orden")[:10]
    estatuses = EstatusOrdenDispositivo.objects.all().order_by('nombre')
    return render(request, "usuarios/dashboard_tecnico.html", {"ordenes_recientes": ordenes_recientes, "estatuses": estatuses})


@solo_staff
def admin_tecnicos(request):
    tecnicos = Tecnico.objects.select_related('usuario').all().order_by('usuario__username')
    return render(request, 'usuarios/admin_tecnicos.html', {'tecnicos': tecnicos})


@solo_staff
def toggle_tecnico_activo(request, tecnico_id):
    tecnico = get_object_or_404(Tecnico, pk=tecnico_id)
    tecnico.activo = not tecnico.activo
    tecnico.save()
    messages.success(request, f"Técnico {'activado' if tecnico.activo else 'desactivado'}: {tecnico.usuario.username}")
    return redirect('admin_tecnicos')


@solo_staff
def borrar_tecnico(request, tecnico_id):
    tecnico = get_object_or_404(Tecnico, pk=tecnico_id)
    if request.method == 'POST':
        username = tecnico.usuario.username
        tecnico.usuario.delete()
        messages.success(request, f"Técnico eliminado: {username}")
        return redirect('admin_tecnicos')
    return render(request, 'usuarios/confirmar_borrar_tecnico.html', {'tecnico': tecnico})
