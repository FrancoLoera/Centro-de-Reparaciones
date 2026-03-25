from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm, AdminUserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import Tecnico, Tecnico_Tipo_Especializacion, Usuario


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class UsuarioAdminCreationForm(AdminUserCreationForm):
    class Meta:
        model = Usuario
        fields = ("correo", "username", "telefono")


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioAdminCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ("correo", "username", "telefono", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("correo", "username", "telefono")
    ordering = ("correo",)

    fieldsets = (
        (None, {"fields": ("correo", "password")}),
        (_("Información personal"), {"fields": ("username", "telefono", "first_name", "last_name", "email")}),
        (
            _("Permisos"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Fechas importantes"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "correo",
                    "username",
                    "telefono",
                    "usable_password",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(Tecnico)
admin.site.register(Tecnico_Tipo_Especializacion)
