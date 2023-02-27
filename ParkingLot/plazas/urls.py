from django.urls import path

from .views import PlazaListado, PlazaDetalle, PlazaCrear, PlazaActualizar, PlazaEliminar

from django.conf import settings

urlpatterns = [
    #path('', views.parkings, name="Parkings"),

    # # La ruta 'ListarParking' en donde listamos todos los registros o Parkings de la Base de Datos
    path('', PlazaListado.as_view(template_name = "plazas/index_plaza.html"), name='ListarPlaza'),    
 
    # # La ruta 'DetalleParking' en donde mostraremos una página con los detalles de un Parking o registro 
    path('DetallePlaza/<int:pk>', PlazaDetalle.as_view(template_name = "plazas/detalle_plaza.html"), name='DetallePlaza'),
 
    # # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Parking o registro  
    path('CrearPlaza', PlazaCrear.as_view(template_name = "plazas/crear_plaza.html"), name='CrearPlazas'),
 
    # # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Parking o registro de la Base de Datos 
    path('ActualizarPlaza/<int:pk>', PlazaActualizar.as_view(template_name = "plazas/actualizar_plaza.html"), name='ActualizarPlaza'), 
 
    # # La ruta 'eliminar' que usaremos para eliminar un Parking o registro de la Base de Datos 
    path('ElminarPlaza/<int:pk>', PlazaEliminar.as_view(), name='ElminarPlaza'),
          
]
