from django.urls import path
from . import views

app_name = 'seguimiento'

urlpatterns = [
    path('seguimiento/estatus/', views.estatus_list, name='estatus_list'),
    path('seguimiento/estatus/nuevo/', views.estatus_create, name='estatus_create'),
    path('seguimiento/estatus/<int:pk>/editar/', views.estatus_edit, name='estatus_edit'),
    path('seguimiento/estatus/<int:pk>/borrar/', views.estatus_delete, name='estatus_delete'),
]
