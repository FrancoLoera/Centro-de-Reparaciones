import uuid

from django.db import models

from apps.clientes.models import Cliente


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True, db_column="idOrden")
    codigo_seguimiento = models.CharField(
        max_length=36,
        unique=True,
        default=uuid.uuid4,
        editable=False,
        db_column="codigoSeguimiento",
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="ordenes",
        db_index=True,
        db_column="idCliente",
    )
    dispositivo = models.ForeignKey(
        'dispositivos.Dispositivo',
        on_delete=models.PROTECT,
        related_name='ordenes',
        db_column='idDispositivo',
        null=True,
        blank=True,
    )
    estatus = models.ForeignKey(
        'seguimiento.EstatusOrdenDispositivo',
        on_delete=models.PROTECT,
        related_name='ordenes',
        db_column='idEstatusOrdenDispositivo',
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "orden"
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

    def __str__(self) -> str:
        return f"Orden {self.id_orden} - {self.codigo_seguimiento}"
