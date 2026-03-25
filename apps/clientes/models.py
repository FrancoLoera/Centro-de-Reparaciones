from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, db_column="idCliente")
    nombre_completo = models.CharField(max_length=100, db_column="nombreCompleto")
    telefono = models.CharField(max_length=20, db_index=True, db_column="telefono")
    telefono_alternativo = models.CharField(max_length=20, null=True, blank=True, db_column="telefonoAlternativo")
    email = models.EmailField(max_length=250, unique=True, null=True, blank=True, db_column="email")

    class Meta:
        db_table = "cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return self.nombre_completo
