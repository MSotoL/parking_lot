"""ParkingLot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from parkings.views import ParkingsListado,ParkingsDetalle,ParkingsCrear,ParkingsActualizar, ParkingsEliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ParkingLotApp.urls')),
    path('contacto/', include('contacto.urls')),
    path('parkings/', include('parkings.urls')),
    path('edificios/', include('edificios.urls')),
    
    # # # La ruta 'ListarParking' en donde listamos todos los registros o Parkings de la Base de Datos
    # path('parkings/', ParkingsListado.as_view(template_name = "parkings/index_parking.html"), name='ListarParking'),    
 
    # # # La ruta 'DetalleParking' en donde mostraremos una página con los detalles de un Parking o registro 
    # path('parkings/DetalleParking/<int:pk>', ParkingsDetalle.as_view(template_name = "parkings/detalle_parking.html"), name='DetalleParking'),
 
    # # # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Parking o registro  
    # path('parkings/CrearParking', ParkingsCrear.as_view(template_name = "parkings/crear_parking.html"), name='CrearParking'),
 
    # # # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Parking o registro de la Base de Datos 
    # path('parkings/ActualizarParking/<int:pk>', ParkingsActualizar.as_view(template_name = "parkings/actualizar_parking.html"), name='ActualizarParking'), 
 
    # # # La ruta 'eliminar' que usaremos para eliminar un Parking o registro de la Base de Datos 
    # path('parkings/ElminarParking/<int:pk>', ParkingsEliminar.as_view(), name='ElminarParking'),    
]
