from django.db import models

# Creo los modelos para los Tipos de Plaza
# Los datos de los Tipos de Plaza NO podrán ser modificados por el usuario
# Los datos de los Tipos de Plaza serán fijos y tendrán los valores:
#       - Plaza Grande
#       - Plaza Pequeña
#       - Plaza Discapacitados

class TipoPlaza(models.Model):
    
    # Creo el modelo de datos de los Tipos de Plaza
    descripcion=models.CharField(max_length=50)
    ancho=models.FloatField()
    largo=models.FloatField()
    discap=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)    
    
    class Meta:
        verbose_name='tipoPlaza'
        verbose_name_plural='tiposPlaza'
    
    def __str__(self):
        return self.descripcion