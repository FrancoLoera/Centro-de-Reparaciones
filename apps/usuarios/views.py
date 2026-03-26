from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.ordenes.models import Orden
from apps.seguimiento.models import EstatusOrdenDispositivo


@login_required
def login_redirect_view(request):
    user = request.user
    
    if user.is_superuser:
        return redirect("admin:index")
    
    if hasattr(user, "perfil_tecnico"):
        return redirect("dashboard_tecnico")
    
    return redirect("dashboard_admin")

@login_required
def dashboard_tecnico(request):

    if not hasattr(request.user, "perfil_tecnico"):
        return redirect("login_redirect")

    ordenes_recientes = Orden.objects.select_related("cliente", "dispositivo", "estatus").order_by("-id_orden")[:10]
    estatuses = EstatusOrdenDispositivo.objects.all().order_by('nombre')
    return render(request, "usuarios/dashboard_tecnico.html", {"ordenes_recientes": ordenes_recientes, "estatuses": estatuses})

@login_required
def dashboard_admin(request):

    if hasattr(request.user, "perfil_tecnico"):
        return redirect("login_redirect")

    ordenes = (
        Orden.objects
        .select_related(
            "cliente",
            "dispositivo",
            "estatus"
        )
        .order_by("-id_orden")[:5]
    )

    return render(
        request,
        "dashboards/admin/dashboard.html",
        {
            "ordenes": ordenes
        }
    )