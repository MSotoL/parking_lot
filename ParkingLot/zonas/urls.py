from django.urls import path

from .views import ZonaListado, ZonaDetalle, ZonaCrear, ZonaActualizar, ZonaEliminar

from django.conf import settings

urlpatterns = [
    #path('', views.parkings, name="Parkings"),

    # # La ruta 'ListarParking' en donde listamos todos los registros o Parkings de la Base de Datos
    path('', ZonaListado.as_view(template_name = "zonas/index_zona.html"), name='ListarZona'),    
 
    # # La ruta 'DetalleParking' en donde mostraremos una página con los detalles de un Parking o registro 
    path('DetalleZona/<int:pk>', ZonaDetalle.as_view(template_name = "zonas/detalle_zona.html"), name='DetalleZona'),
 
    # # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Parking o registro  
    path('CrearZona', ZonaCrear.as_view(template_name = "zonas/crear_zona.html"), name='CrearZonas'),
 
    # # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Parking o registro de la Base de Datos 
    path('ActualizarZona/<int:pk>', ZonaActualizar.as_view(template_name = "zonas/actualizar_zona.html"), name='ActualizarZona'), 
 
    # # La ruta 'eliminar' que usaremos para eliminar un Parking o registro de la Base de Datos 
    path('ElminarZona/<int:pk>', ZonaEliminar.as_view(), name='ElminarZona'),
          
]
