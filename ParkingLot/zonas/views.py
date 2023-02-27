from django.shortcuts import render

# Instancio las vistas genéricas de Django
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instancio los modelos de la BBDD
from .models import Zona
from plantas.models import Planta

# Sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class ZonaListado(ListView): 
    model = Zona # Llamo a la clase 'Zona' que se encuentra en el archivo 'models.py'

class ZonaCrear(SuccessMessageMixin, CreateView): 
    model = Zona # Llamamos a la clase 'Zona' que se encuentra en nuestro archivo 'models.py'
    form = Zona # Definimos nuestro formulario con el nombre de la clase o modelo 'Zona'
    fields = ("descripcion", "observaciones", "id_planta") # Le decimos a Django que muestre los campos de la tabla 'Zona' de nuestra Base de Datos 
    
    success_message = 'Zona Creada Correctamente' # Mostramos este Mensaje si el Parking se crea correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):        
        return reverse('ListarZona') # Redireccionamos a la vista principal 'ListarParking'
    
class ZonaDetalle(DetailView): 
    model = Zona # Llamamos a la clase 'Zona' que se encuentra en nuestro archivo 'models.py' 
    

class ZonaActualizar(SuccessMessageMixin, UpdateView): 
    model = Zona # Llamamos a la clase 'Zona' que se encuentra en nuestro archivo 'models.py' 
    form = Zona # Definimos nuestro formulario con el nombre de la clase o modelo 'Zona' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Zona' de nuestra Base de Datos 
    success_message = 'Zona Actualizada Correctamente' # Mostramos este Mensaje si el Zona se edita correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):               
        return reverse('ListarZona') # Redireccionamos a la vista principal 



class ZonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Zona
    form = Zona
    fields = "__all__"     
 
    # Redireccionamos a la página principal 
    def get_success_url(self): 
        success_message = 'Zona Eliminada Correctamente' # Mostramos este Mensaje si el Parking se ha eliminado correctamente
        messages.success (self.request, (success_message))       
        return reverse('ListarZona') # Redireccionamos a la vista principal 