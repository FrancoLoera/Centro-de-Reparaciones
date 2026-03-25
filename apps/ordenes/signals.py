from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
import os

from .models import Orden


@receiver(post_save, sender=Orden)
def generar_pagina_publica(sender, instance: Orden, created, **kwargs):
    """Generate a static HTML page for the order inside templates/ordenes/public/{codigo}.html"""
    try:
        codigo = str(instance.codigo_seguimiento)
        base_dir = os.path.dirname(__file__)
        public_dir = os.path.join(base_dir, 'templates', 'ordenes', 'public')
        os.makedirs(public_dir, exist_ok=True)
        html = render_to_string('ordenes/public_order_template.html', {'orden': instance})
        public_file = os.path.join(public_dir, f"{codigo}.html")
        with open(public_file, 'w', encoding='utf-8') as f:
            f.write(html)
    except Exception:
        # Avoid raising errors during save
        pass
