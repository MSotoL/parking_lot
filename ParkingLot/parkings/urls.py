from django.urls import path

from . import views
from django.conf import settings

urlpatterns = [
    path('', views.parkings, name="Parkings"),
    
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('', ParkingsListado.as_view(template_name = "index_parking.html"), name='listarparking'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('detalle/<int:pk>', ParkingsDetalle.as_view(template_name = "detalle_parking.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('crear', ParkingsCrear.as_view(template_name = "crear_parking.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('editar/<int:pk>', ParkingsActualizar.as_view(template_name = "actualizar_parking.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('eliminar/<int:pk>', ParkingsEliminar.as_view(), name='eliminar'),     
]
