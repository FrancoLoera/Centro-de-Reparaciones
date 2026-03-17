from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

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

    return HttpResponse("Panel Administrativo")