from django.contrib import admin
from .models import EstatusOrdenDispositivo, TipoComentario, Orden, OrdenDispositivo, HistorialOrdenDispositivo, Comentario

# Register your models here.
admin.site.register(EstatusOrdenDispositivo)
admin.site.register(TipoComentario)
admin.site.register(Orden)
admin.site.register(OrdenDispositivo)
admin.site.register(HistorialOrdenDispositivo)
admin.site.register(Comentario)