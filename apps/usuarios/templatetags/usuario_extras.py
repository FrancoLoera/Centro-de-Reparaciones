from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter(name="es_tecnico")
def es_tecnico_filter(user):
    if not getattr(user, "is_authenticated", False):
        return False
    try:
        user.perfil_tecnico
        return True
    except ObjectDoesNotExist:
        return False
