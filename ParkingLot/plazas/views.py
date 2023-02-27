from django.shortcuts import render

# Instancio las vistas genéricas de Django
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instancio los modelos de la BBDD
from .models import Plaza
from zonas.models import Zona
from ParkingLotApp.models import TipoPlaza

# Sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class PlazaListado(ListView): 
    model = Plaza # Llamo a la clase 'Plaza' que se encuentra en el archivo 'models.py'

class PlazaCrear(SuccessMessageMixin, CreateView): 
    model = Plaza # Llamamos a la clase 'Plaza' que se encuentra en nuestro archivo 'models.py'
    form = Plaza # Definimos nuestro formulario con el nombre de la clase o modelo 'Plaza'
    fields = ("descripcion", "observaciones", "id_zona", "id_tipo_plaza") # Le decimos a Django que muestre los campos de la tabla 'Plaza' de nuestra Base de Datos 
    
    success_message = 'Plaza Creada Correctamente' # Mostramos este Mensaje si el Parking se crea correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):        
        return reverse('ListarPlaza') # Redireccionamos a la vista principal 'ListarPlaza'
    
class PlazaDetalle(DetailView): 
    model = Plaza # Llamamos a la clase 'Plaza' que se encuentra en nuestro archivo 'models.py' 
    

class PlazaActualizar(SuccessMessageMixin, UpdateView): 
    model = Plaza # Llamamos a la clase 'Plaza' que se encuentra en nuestro archivo 'models.py' 
    form = Plaza # Definimos nuestro formulario con el nombre de la clase o modelo 'Plaza' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Plaza' de nuestra Base de Datos 
    success_message = 'Plaza Actualizada Correctamente' # Mostramos este Mensaje si el Plaza se edita correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):               
        return reverse('ListarPlaza') # Redireccionamos a la vista principal 



class PlazaEliminar(SuccessMessageMixin, DeleteView): 
    model = Plaza
    form = Plaza
    fields = "__all__"     
 
    # Redireccionamos a la página principal 
    def get_success_url(self): 
        success_message = 'Plaza Eliminada Correctamente' # Mostramos este Mensaje si la Plaza se ha eliminado correctamente
        messages.success (self.request, (success_message))       
        return reverse('ListarPlaza') # Redireccionamos a la vista principal 