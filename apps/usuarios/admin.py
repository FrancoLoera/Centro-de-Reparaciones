from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Tecnico, Tecnico_Tipo_Especializacion

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    model = Usuario

    list_display = ("email", "username", "telefono", "is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Información personal", {"fields": ("username", "telefono")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "telefono", "password1", "password2"),
        }),
    )

    ordering = ("email",)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "activo")

admin.site.register(Tecnico_Tipo_Especializacion)