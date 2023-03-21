from django.urls import path

from parkings.views import ParkingsListado,ParkingsDetalle,ParkingsCrear,ParkingsActualizar, ParkingsEliminar

# ****************************************************
# ****************************************************
# from edificios.urls import EdificioListadoFiltrado
# ****************************************************
# ****************************************************

from django.conf import settings

urlpatterns = [
    #path('', views.parkings, name="Parkings"),

    # # La ruta 'ListarParking' en donde listamos todos los registros o Parkings de la Base de Datos
    path('', ParkingsListado.as_view(template_name = "parkings/index_parking.html"), name='ListarParking'),    
 
    # # La ruta 'DetalleParking' en donde mostraremos una página con los detalles de un Parking o registro 
    path('DetalleParking/<int:pk>', ParkingsDetalle.as_view(template_name = "parkings/detalle_parking.html"), name='DetalleParking'),
 
    # # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Parking o registro  
    path('CrearParking', ParkingsCrear.as_view(template_name = "parkings/crear_parking.html"), name='CrearParking'),
 
    # # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Parking o registro de la Base de Datos 
    path('ActualizarParking/<int:pk>', ParkingsActualizar.as_view(template_name = "parkings/actualizar_parking.html"), name='ActualizarParking'), 
 
    # # La ruta 'eliminar' que usaremos para eliminar un Parking o registro de la Base de Datos 
    path('ElminarParking/<int:pk>', ParkingsEliminar.as_view(), name='ElminarParking'),   
    
    # path('edificios/ListarEdificioFiltrado/<int:parking>/', EdificioListadoFiltrado.as_view(template_name = "edificios/index_edificio_filtrado.html"), name='ListarEdificioFiltrado'),    
]
