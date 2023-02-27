from django.shortcuts import render

# Instancio las vistas genéricas de Django
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instancio los modelos de la BBDD
from .models import Edificio
from parkings.models import Parking

# Sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class EdificioListado(ListView): 
    model = Edificio # Llamo a la clase 'Edificio' que se encuentra en el archivo 'models.py'

class EdificioCrear(SuccessMessageMixin, CreateView): 
    model = Edificio # Llamamos a la clase 'Edificio' que se encuentra en nuestro archivo 'models.py'
    form = Edificio # Definimos nuestro formulario con el nombre de la clase o modelo 'Edificio'
    fields = ("descripcion", "observaciones", "id_parking") # Le decimos a Django que muestre los campos de la tabla 'Edificio' de nuestra Base de Datos 
    
    success_message = 'Edificio Creado Correctamente' # Mostramos este Mensaje si el Parking se crea correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):        
        return reverse('ListarEdificio') # Redireccionamos a la vista principal 'ListarParking'
    
class EdificioDetalle(DetailView): 
    model = Edificio # Llamamos a la clase 'Edificio' que se encuentra en nuestro archivo 'models.py' 
    


class EdificioActualizar(SuccessMessageMixin, UpdateView): 
    model = Edificio # Llamamos a la clase 'Edificio' que se encuentra en nuestro archivo 'models.py' 
    form = Edificio # Definimos nuestro formulario con el nombre de la clase o modelo 'Edificio' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Edificio' de nuestra Base de Datos 
    success_message = 'Edificio Actualizado Correctamente' # Mostramos este Mensaje si el Edificio se edita correctamente
 
    # Redireccionamos a la página principal 
    def get_success_url(self):               
        return reverse('ListarEdificio') # Redireccionamos a la vista principal 



class EdificioEliminar(SuccessMessageMixin, DeleteView): 
    model = Edificio
    form = Edificio
    fields = "__all__"     
 
    # Redireccionamos a la página principal 
    def get_success_url(self): 
        success_message = 'Edificio Eliminado Correctamente' # Mostramos este Mensaje si el Parking se ha eliminado correctamente
        messages.success (self.request, (success_message))       
        return reverse('ListarEdificio') # Redireccionamos a la vista principal 