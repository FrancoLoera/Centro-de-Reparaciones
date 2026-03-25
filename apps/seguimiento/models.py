from django.db import models
from apps.clientes.models import Cliente
from apps.dispositivos.models import Dispositivo


class EstatusOrdenDispositivo(models.Model):
    id_estatus = models.AutoField(primary_key=True, db_column="idEstatusOrdenDispositivo")
    nombre = models.CharField(max_length=20, unique=True, db_column="nombre")

    class Meta:
        db_table = "estatus_orden_dispositivo"

    def __str__(self):
        return self.nombre


class OrdenDispositivo(models.Model):
    id_orden_dispositivo = models.AutoField(primary_key=True, db_column="idOrdenDispositivo")
    orden = models.ForeignKey(
        'ordenes.Orden', on_delete=models.CASCADE, db_column="idOrden", related_name="orden_dispositivos"
    )
    dispositivo = models.ForeignKey(
        Dispositivo, on_delete=models.PROTECT, db_column="idDispositivo", related_name="orden_dispositivos"
    )
    fecha_inicio = models.DateTimeField(null=True, blank=True, db_column="fechaInicio")
    fecha_fin = models.DateTimeField(null=True, blank=True, db_column="fechaFin")
    id_tipo_soporte = models.PositiveSmallIntegerField(null=True, blank=True, db_column="idTipoSoporte")
    id_tipo_dispositivo = models.PositiveSmallIntegerField(null=True, blank=True, db_column="idTipoDispositivo")

    class Meta:
        db_table = "orden_dispositivo"
        indexes = [
            models.Index(fields=["orden"], name="idx_ord_orden"),
            models.Index(fields=["dispositivo"], name="idx_ord_dispositivo"),
            models.Index(fields=["fecha_fin"], name="idx_ord_fechaFin"),
        ]


class HistorialOrdenDispositivo(models.Model):
    id_historial = models.AutoField(primary_key=True, db_column="idHistorial")
    fecha_asignacion = models.DateTimeField(db_column="fechaAsignacion")
    fecha_fin = models.DateTimeField(null=True, blank=True, db_column="fechaFin")
    id_estatus = models.ForeignKey(EstatusOrdenDispositivo, on_delete=models.PROTECT, db_column="idEstatusOrdenDispositivo", related_name="historials")
    id_orden_dispositivo = models.ForeignKey(OrdenDispositivo, on_delete=models.CASCADE, db_column="idOrdenDispositivo", related_name="historials")
    id_tecnico = models.PositiveSmallIntegerField(db_column="idTecnico")

    class Meta:
        db_table = "historial_orden_dispositivo"
        indexes = [
            models.Index(fields=["id_tecnico"], name="idx_hist_idTec"),
            models.Index(fields=["id_estatus", "fecha_fin"], name="idx_hist_est_f"),
        ]


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True, db_column="idComentario")
    orden_dispositivo = models.ForeignKey(OrdenDispositivo, on_delete=models.CASCADE, db_column="idOrdenDispositivo", related_name="comentarios")
    comentario = models.TextField(db_column="comentario")
    fecha_creacion = models.DateTimeField(db_column="fechaCreacion")
    id_tecnico = models.PositiveSmallIntegerField(null=True, blank=True, db_column="idTecnico")
    id_tipo_comentario = models.PositiveSmallIntegerField(db_column="idTipoComentario")

    class Meta:
        db_table = "comentario"
        indexes = [models.Index(fields=["orden_dispositivo"], name="idx_com_orden")]


# End of seguimiento models
