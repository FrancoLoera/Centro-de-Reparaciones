from django.urls import path

from .views import (
    LoginTecnicoView,
    LogoutTecnicoView,
    dashboard_tecnico,
    portal_publico,
    admin_tecnicos,
    toggle_tecnico_activo,
    borrar_tecnico,
)


urlpatterns = [
    path("", portal_publico, name="portal_publico"),
    path("acceder/", LoginTecnicoView.as_view(), name="login_tecnico"),
    path("salir/", LogoutTecnicoView.as_view(), name="logout_tecnico"),
    path("panel/", dashboard_tecnico, name="dashboard_tecnico"),

    # Panel administrativo (solo staff)
    path("admin/tecnicos/", admin_tecnicos, name="admin_tecnicos"),
    path("admin/tecnicos/<int:tecnico_id>/toggle/", toggle_tecnico_activo, name="toggle_tecnico_activo"),
    path("admin/tecnicos/<int:tecnico_id>/borrar/", borrar_tecnico, name="borrar_tecnico"),
]
