from django.urls import path

from .views import EdificioListado, EdificioDetalle, EdificioCrear, EdificioActualizar, EdificioEliminar

from django.conf import settings

urlpatterns = [
    #path('', views.parkings, name="Parkings"),

    # La ruta 'ListarEdificio' en donde listamos todos los registros o Parkings de la Base de Datos
    path('', EdificioListado.as_view(template_name = "edificios/index_edificio.html"), name='ListarEdificio'),    
 
    # La ruta 'DetalleEdificio' en donde mostraremos una página con los detalles de un Parking o registro 
    path('DetalleEdificio/<int:pk>', EdificioDetalle.as_view(template_name = "edificios/detalle_edificio.html"), name='DetalleEdificio'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Parking o registro  
    path('CrearEdificio', EdificioCrear.as_view(template_name = "edificios/crear_edificio.html"), name='CrearEdificios'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Parking o registro de la Base de Datos 
    path('ActualizarEdificio/<int:pk>', EdificioActualizar.as_view(template_name = "edificios/actualizar_edificio.html"), name='ActualizarEdificio'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Parking o registro de la Base de Datos 
    path('ElminarEdificio/<int:pk>', EdificioEliminar.as_view(), name='ElminarEdificio'),
]
