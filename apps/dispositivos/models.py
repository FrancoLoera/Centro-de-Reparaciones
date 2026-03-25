from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "marca"
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self) -> str:
        return self.nombre


class Dispositivo(models.Model):
    alias = models.CharField(max_length=100)
    numero_serie = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Número de serie del equipo (opcional).",
    )
    color = models.CharField(max_length=30)
    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name="dispositivos",
    )

    class Meta:
        db_table = "dispositivo"
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def __str__(self) -> str:
        return f"{self.alias} ({self.marca})"
