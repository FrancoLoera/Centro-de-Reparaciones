from django.contrib import admin
from .models import Usuario, Tecnico, Tecnico_Tipo_Especializacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tecnico)
admin.site.register(Tecnico_Tipo_Especializacion)