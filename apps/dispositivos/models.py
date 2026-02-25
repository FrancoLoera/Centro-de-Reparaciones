from django.db import models


class Marca(models.Model):
    """
    Representa la marca de un dispositivo.

    Equivalente a la tabla MARCA:
    - idMarca TINYINT UNSIGNED PK
    - nombre VARCHAR(30) UNIQUE
    """

    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "marca"
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self) -> str:
        return self.nombre


class Dispositivo(models.Model):
    """
    Representa un equipo que ingresa al centro de reparaciones.

    Equivalente a la tabla DISPOSITIVO:
    - idDispositivo MEDIUMINT UNSIGNED PK
    - alias VARCHAR(100)
    - numeroSerie VARCHAR(50) NULL
    - color VARCHAR(30)
    - marca TINYINT UNSIGNED FK -> MARCA.idMarca
    """

    id_dispositivo = models.AutoField(primary_key=True)
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
