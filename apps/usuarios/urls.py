from django.urls import path

from .views import (
    LoginTecnicoView,
    LogoutTecnicoView,
    dashboard_tecnico,
    portal_publico,
)


urlpatterns = [
    path("", portal_publico, name="portal_publico"),
    path("acceder/", LoginTecnicoView.as_view(), name="login_tecnico"),
    path("salir/", LogoutTecnicoView.as_view(), name="logout_tecnico"),
    path("panel/", dashboard_tecnico, name="dashboard_tecnico"),
]
