from django.shortcuts import render

# Instancio las vistas genéricas de Django
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instancio los modelos de la BBDD
from .models import Planta
from parkings.models import Parking

# Sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class PlantaListado(ListView): 
    model = Planta # Llamo a la clase 'Planta' que se encuentra en el archivo 'models.py'

class PlantaCrear(SuccessMessageMixin, CreateView): 
    model = Planta # Llamamos a la clase 'Planta' que se encuentra en nuestro archivo 'models.py'
    form = Planta # Definimos nuestro formulario con el nombre de la clase o modelo 'Planta'
    fields = ("descripcion", "max_plazas", "observaciones", "id_edificio") # Le decimos a Django que muestre los campos de la tabla 'Planta' de nuestra Base de Datos 
    
    success_message = 'Planta Creada Correctamente' # Mostramos este Mensaje si el Parking se crea correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):        
        return reverse('ListarPlanta') # Redireccionamos a la vista principal 'ListarParking'
    
class PlantaDetalle(DetailView): 
    model = Planta # Llamamos a la clase 'Planta' que se encuentra en nuestro archivo 'models.py' 
    
class PlantaActualizar(SuccessMessageMixin, UpdateView): 
    model = Planta # Llamamos a la clase 'Planta' que se encuentra en nuestro archivo 'models.py' 
    form = Planta # Definimos nuestro formulario con el nombre de la clase o modelo 'Planta' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Planta' de nuestra Base de Datos 
    success_message = 'Planta Actualizada Correctamente' # Mostramos este Mensaje si el Planta se edita correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):               
        return reverse('ListarPlanta') # Redireccionamos a la vista principal 

class PlantaEliminar(SuccessMessageMixin, DeleteView): 
    model = Planta
    form = Planta
    fields = "__all__"     
 
    # Redireccionamos a la página principal 
    def get_success_url(self): 
        success_message = 'Planta Eliminada Correctamente' # Mostramos este Mensaje si el Parking se ha eliminado correctamente
        messages.success (self.request, (success_message))       
        return reverse('ListarPlanta') # Redireccionamos a la vista principal 
    
class PlantaDibujar(DetailView):
    model = Planta
    
    def get_success_url(self): 
        return reverse('DibujarPlanta') # Redireccionamos a la vista principal 