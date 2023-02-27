from django.db import models
from parkings.models import Parking

# Creo los modelos para el Parking
# Los datos de los Parkings podrán ser modificados por el usuario

class Edificio(models.Model):
    
    # Creo el modelo de datos del Edificio
    descripcion=models.CharField(max_length=50)
    observaciones=models.TextField(max_length=300, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    id_parking=models.ForeignKey(Parking, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='edificio'
        verbose_name_plural='edificios'
    
    def __str__(self):
        return self.descripcion