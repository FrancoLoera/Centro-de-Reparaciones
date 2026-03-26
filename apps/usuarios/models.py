from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.catalogos.models import Tipo_Soporte, Tipo_Dispositivo

class Usuario(AbstractUser):

    telefono = models.CharField(max_length=20, unique=True)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} - {self.email}"
    
class Tecnico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name = 'perfil_tecnico')
    
    activo = models.BooleanField(default = True) # is_active solo nos sirve para verificar que pueda ingresar al sistema. activo sirve para saber que puede recibir órdenes
    
    def soportes_por_dispositivo(self, dispositivo):
        soportes = self.especializaciones.filter(tipo_dispositivo = dispositivo).values_list('tipo_soporte', flat = True)
        
        soportes = list(soportes)
        
        if Tipo_Soporte.HARDWARE in soportes and Tipo_Soporte.SOFTWARE in soportes:
            return "AMBOS"
        
        return soportes
    
    def __str__(self):
        return f"Tecnico: {self.usuario.username}"

class Tecnico_Tipo_Especializacion(models.Model):
    tecnico = models.ForeignKey(Tecnico, on_delete = models.CASCADE, related_name = 'especializaciones')
    
    tipo_dispositivo = models.ForeignKey(Tipo_Dispositivo, on_delete = models.CASCADE)
    
    tipo_soporte = models.CharField(max_length = 10, choices = Tipo_Soporte.choices)
    
    class Meta:
        unique_together = ('tecnico', 'tipo_dispositivo', 'tipo_soporte')
        
    def __str__(self):
        return f"{self.tecnico.usuario.username} - {self.tipo_dispositivo} - {self.tipo_soporte}"