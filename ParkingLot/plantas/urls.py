from django.urls import path

from .views import PlantaListado, PlantaDetalle, PlantaCrear, PlantaActualizar, PlantaEliminar, PlantaDibujar

from django.conf import settings

urlpatterns = [
    #path('', views.parkings, name="Parkings"),

    # La ruta 'ListarParking' en donde listamos todos los registros o Parkings de la Base de Datos
    path('', PlantaListado.as_view(template_name = "plantas/index_planta.html"), name='ListarPlanta'),    
 
    # La ruta 'DetalleParking' en donde mostraremos una página con los detalles de un Parking o registro 
    path('DetallePlanta/<int:pk>', PlantaDetalle.as_view(template_name = "plantas/detalle_planta.html"), name='DetallePlanta'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Parking o registro  
    path('CrearPlanta', PlantaCrear.as_view(template_name = "plantas/crear_planta.html"), name='CrearPlantas'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Parking o registro de la Base de Datos 
    path('ActualizarPlanta/<int:pk>', PlantaActualizar.as_view(template_name = "plantas/actualizar_planta.html"), name='ActualizarPlanta'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Parking o registro de la Base de Datos 
    path('ElminarPlanta/<int:pk>', PlantaEliminar.as_view(), name='ElminarPlanta'),
    
    # La ruta 'dibujar' que usaremos para diseñar el layout de un Parking 
    path('DibujarPlanta/<int:pk>', PlantaDibujar.as_view(template_name = "plantas/planta_layout.html"), name='DibujarPlanta'),    
          
]
