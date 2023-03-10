from django.db import models

# Creo los modelos para el Parking
# Los datos de los Parkings podrán ser modificados por el usuario

class Parking(models.Model):
    
    # Creo el modelo de datos del Parking
    descripcion=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=100)
    cubierto=models.BooleanField(default=False)
    observaciones=models.TextField(max_length=300, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='parking'
        verbose_name_plural='parkings'
    
    def __str__(self):
        return self.descripcion