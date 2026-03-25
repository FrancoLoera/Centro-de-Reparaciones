from functools import wraps

from django.conf import settings
from django.contrib.auth.views import redirect_to_login


def es_tecnico(user):
    return user.is_authenticated and hasattr(user, "perfil_tecnico")


def solo_tecnicos(view_func):
    """
    Solo usuarios con perfil Tecnico acceden al panel operativo.
    Anonimos -> login de tecnicos. Autenticado sin perfil -> pagina de denegacion.
    """

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), settings.LOGIN_URL)
        if not hasattr(request.user, "perfil_tecnico"):
            return _respuesta_no_tecnico(request)
        return view_func(request, *args, **kwargs)

    return _wrapped


def _respuesta_no_tecnico(request):
    from django.shortcuts import render

    return render(
        request,
        "usuarios/sin_acceso_tecnico.html",
        {
            "es_staff": request.user.is_staff,
        },
        status=403,
    )
