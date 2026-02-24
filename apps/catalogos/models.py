from django.db import models

# Create your models here.
class Tipo_Dispositivo(models.Model):
    nombre = models.CharField(max_length = 30, unique = True)
    
    def __str__(self):
        return self.nombre
    
class Tipo_Soporte(models.TextChoices):
    HARDWARE = "HARDWARE", "Hardware"
    SOFTWARE = "SOFTWARE", "Software"
    AMBOS = "AMBOS", "Ambos"