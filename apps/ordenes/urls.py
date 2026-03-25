from django.urls import path

from . import views


urlpatterns = [
    path("ordenes/", views.lista_ordenes, name="ordenes_lista"),
    path("ordenes/nueva/", views.crear_orden, name="ordenes_crear"),
    path("ordenes/<int:pk>/editar/", views.editar_orden, name="ordenes_editar"),
    path("ordenes/<int:pk>/borrar/", views.borrar_orden, name="ordenes_borrar"),
    path("ordenes/<int:pk>/cambiar_estatus/", views.cambiar_estatus, name="ordenes_cambiar_estatus"),
    path("ordenes/public/<str:codigo>/", views.orden_publica, name="ordenes_publica"),
]
