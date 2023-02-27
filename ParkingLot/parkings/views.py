from django.shortcuts import render

# Instancio las vistas genéricas de Django
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

# Instancio los modelos de la BBDD
from .models import Parking

class ParkingsListado(ListView): 
    model = Parking # Llamo a la clase 'Parking' que se encuentra en el archivo 'models.py' 


class ParkingsCrear(SuccessMessageMixin, CreateView): 
    model = Parking # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Parking # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Parking Creado Correctamente' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('listarparking') # Redireccionamos a la vista principal 'leer'
    
    
    
class ParkingsDetalle(DetailView): 
    model = Parking # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    


class ParkingsActualizar(SuccessMessageMixin, UpdateView): 
    model = Parking # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Parking # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Parking Actualizado Correctamente' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('listarparking') # Redireccionamos a la vista principal 'leer'



class ParkingEliminar(SuccessMessageMixin, DeleteView): 
    model = Parking
    form = Parking
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Parking Eliminado Correctamente' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('listarparking') # Redireccionamos a la vista principal 'leer'