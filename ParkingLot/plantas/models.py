from django.db import models
from edificios.models import Edificio

# Creo los modelos para las Plantas
# Los datos de las Plantas podrán ser modificadas por el usuario

# Create your models here.
class Planta(models.Model):
    
    # Creo el modelo de datos de la Planta
    descripcion=models.CharField(max_length=50)
    max_plazas=models.IntegerField(blank=False, default=0)
    observaciones=models.TextField(max_length=300, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    id_edificio=models.ForeignKey(Edificio, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='planta'
        verbose_name_plural='plantas'
    
    def __str__(self):
        return self.descripcion