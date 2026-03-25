from django.urls import path

from . import views


urlpatterns = [
    path("dispositivos/", views.lista_dispositivos, name="dispositivos_lista"),
    path(
        "dispositivos/nuevo/",
        views.crear_dispositivo,
        name="dispositivos_crear",
    ),
    path(
        "dispositivos/<int:pk>/editar/",
        views.editar_dispositivo,
        name="dispositivos_editar",
    ),
    path(
        "dispositivos/<int:pk>/borrar/",
        views.borrar_dispositivo,
        name="dispositivos_borrar",
    ),
    path("marcas/", views.lista_marcas, name="marcas_lista"),
    path("marcas/nueva/", views.crear_marca, name="marcas_crear"),
    path(
        "marcas/<int:pk>/editar/",
        views.editar_marca,
        name="marcas_editar",
    ),
    path(
        "marcas/<int:pk>/borrar/",
        views.borrar_marca,
        name="marcas_borrar",
    ),
]
