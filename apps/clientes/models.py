from django.db import models

class Cliente(models.Model):

    nombreCompleto = models.CharField(
        max_length=100
    )

    telefono = models.CharField(
        max_length=20,
        db_index=True
    )

    telefonoAlternativo = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    email = models.EmailField(
        max_length=250,
        null=True,
        blank=True,
        unique=True
    )

    class Meta:
        db_table = "CLIENTE"

    def __str__(self):
        return self.nombreCompleto