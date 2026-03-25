from django.urls import path

from . import views


urlpatterns = [
    path("clientes/", views.lista_clientes, name="clientes_lista"),
    path("clientes/nuevo/", views.crear_cliente, name="clientes_crear"),
]
