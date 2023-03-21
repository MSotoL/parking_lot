from django.db import models
from zonas.models import Zona
from ParkingLotApp.models import TipoPlaza

# Creo los modelos para las Plazas
# Los datos de las Plantas podrán ser modificadas por el usuario

# Create your models here.
class Plaza(models.Model):
    
    # Creo el modelo de datos de la Planta
    descripcion=models.CharField(max_length=50)
    observaciones=models.TextField(max_length=300, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    id_zona=models.ForeignKey(Zona, on_delete=models.CASCADE)
    id_tipo_plaza=models.ForeignKey(TipoPlaza, on_delete=models.CASCADE)    
        
    class Meta:
        verbose_name='plaza'
        verbose_name_plural='plazas'
    
    def __str__(self):
        return self.descripcion