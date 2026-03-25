from django.contrib import admin

from .models import Dispositivo, Marca


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("id_marca", "nombre")
    search_fields = ("nombre",)


@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ("id_dispositivo", "alias", "marca", "color", "numero_serie")
    list_filter = ("marca",)
    search_fields = ("alias", "numero_serie")
