from django.db import models
from plantas.models import Planta

# Creo los modelos para el Parking
# Los datos de las Plantas podrán ser modificadas por el usuario

# Create your models here.
class Zona(models.Model):
    
    # Creo el modelo de datos de la Planta
    descripcion=models.CharField(max_length=50)
    observaciones=models.TextField(max_length=300, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    id_planta=models.ForeignKey(Planta, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='zona'
        verbose_name_plural='zonas'
    
    def __str__(self):
        return self.descripcion
