from django.db import models
from apps.catalogos.models import Tipo_Soporte
import uuid

class EstatusOrdenDispositivo(models.Model):

    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    class Meta:
        db_table = "estatus_orden_dispositivo"
    
    def __str__(self):
        return self.nombre

class TipoComentario(models.Model):

    nombre = models.CharField(
        max_length=15,
        unique=True
    )

    class Meta:
        db_table = "tipo_comentario"

    def __str__(self):
        return self.nombre

class Orden(models.Model):

    codigo_seguimiento = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.PROTECT,
        related_name="ordenes",
        db_index=True
    )

    class Meta:
        db_table = "orden"
        
class OrdenDispositivo(models.Model):

    orden = models.ForeignKey(
        "ordenes.Orden",
        on_delete=models.PROTECT
    )

    dispositivo = models.ForeignKey(
        "dispositivos.Dispositivo",
        on_delete=models.PROTECT
    )

    tipo_soporte = models.CharField(
        max_length=8,
        choices=Tipo_Soporte.choices
    )

    tipo_dispositivo = models.ForeignKey(
        "catalogos.Tipo_Dispositivo",
        on_delete=models.PROTECT
    )

    fecha_inicio = models.DateTimeField(
        null=True,
        blank=True
    )

    fecha_fin = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True
    )

    class Meta:
        db_table = "orden_dispositivo"
        constraints = [
            models.UniqueConstraint(
                fields=["orden", "dispositivo"],
                name="unique_orden_dispositivo"
            )
        ]

class HistorialOrdenDispositivo(models.Model):

    fecha_asignacion = models.DateTimeField()

    fecha_fin = models.DateTimeField(
        null=True,
        blank=True
    )

    estatus = models.ForeignKey(
        EstatusOrdenDispositivo,
        on_delete=models.PROTECT
    )

    orden_dispositivo = models.ForeignKey(
        OrdenDispositivo,
        on_delete=models.CASCADE
    )

    tecnico = models.ForeignKey(
        "usuarios.Tecnico",
        on_delete=models.PROTECT,
        db_index=True
    )

    class Meta:
        db_table = "historial_orden_dispositivo"
        indexes = [
            models.Index(
                fields=["estatus", "fecha_fin"]
            )
        ]
        
class Comentario(models.Model):

    orden_dispositivo = models.ForeignKey(
        OrdenDispositivo,
        on_delete=models.CASCADE,
        db_index=True
    )

    comentario = models.TextField()

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    tecnico = models.ForeignKey(
        "usuarios.Tecnico",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    tipo_comentario = models.ForeignKey(
        TipoComentario,
        on_delete=models.PROTECT
    )

    class Meta:
        db_table = "comentario"
        