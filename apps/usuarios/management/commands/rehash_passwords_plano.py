from django.core.management.base import BaseCommand

from apps.usuarios.models import Usuario


class Command(BaseCommand):
    help = (
        "Convierte contraseñas guardadas en texto plano (admin sin UserAdmin) "
        "a hash de Django, manteniendo la misma contraseña."
    )

    def handle(self, *args, **options):
        n = 0
        for u in Usuario.objects.iterator():
            p = u.password or ""
            if "$" in p:
                continue
            if not p.strip():
                continue
            raw = p
            u.set_password(raw)
            u.save(update_fields=["password"])
            self.stdout.write(self.style.SUCCESS(f"Re-hasheado: {u.correo}"))
            n += 1
        if n == 0:
            self.stdout.write("Nada que corregir (todas parecen hasheadas).")
        else:
            self.stdout.write(self.style.SUCCESS(f"Listo: {n} usuario(s)."))
