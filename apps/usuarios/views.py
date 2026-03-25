from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from apps.ordenes.models import OrdenDispositivo
from django.db.models import F
from django.db.models import OuterRef, Subquery
from apps.ordenes.models import HistorialOrdenDispositivo

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

    return HttpResponse("Panel Técnico")


@login_required
def dashboard_admin(request):

    if hasattr(request.user, "perfil_tecnico"):
        return redirect("login_redirect")

    estatus_actual = (
        HistorialOrdenDispositivo.objects
        .filter(
            orden_dispositivo=OuterRef("pk"),
            fecha_fin__isnull=True
        )
        .values("estatus__nombre")[:1]
    )
    
#     tecnico_subquery = (
#     HistorialOrdenDispositivo.objects
#     .filter(
#         orden_dispositivo=OuterRef("pk"),
#         fecha_fin__isnull=True
#     )
#     .values("tecnico__nombre")[:1]
# )

    ordenes = (
    OrdenDispositivo.objects
    .select_related(
        "orden",
        "orden__cliente"
    )
    .annotate(
        estatus_actual=Subquery(estatus_actual),
        # tecnico_actual=Subquery(tecnico_subquery)
    )
    .filter(
        historialordendispositivo__fecha_fin__isnull=True
    )
    .order_by("-fecha_inicio")[:5]
    )

    return render(
        request,
        "dashboards/admin/dashboard.html",
        {
            "ordenes": ordenes
        }
    )