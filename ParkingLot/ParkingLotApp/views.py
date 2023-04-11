
import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from plazas.models import Plaza
from plantas.models import Planta
from .models import TipoPlaza

# Create your views here.

# Vista de la página inicial
def home(request):
    
    #return HttpResponse("Home")
    
    return render(request, "ParkingLotApp/home.html")

def guardarPlazaBD(request):
    
    data={'resultado':'OK', 'mensaje':'Dato insertado'}    
    json_data=json.loads(request.POST.get('plaza'))
    
    # return JsonResponse(json_data, safe=False)
    plantaBD=Planta.objects.get(id=json_data["planta"])
    tipoPlazaBD=TipoPlaza.objects.get(id=json_data["tipo"])
    
    plzBD = Plaza(descripcion=json_data["descripcion"], observaciones=json_data["observaciones"], id_planta=plantaBD, id_tipo_plaza=tipoPlazaBD)
    plzBD.save()
    
    
    data={'resultado':'OK', 'mensaje':'Plaza insertada correctamente.', 'id': plzBD.id}
    
    return JsonResponse(data, safe=False)

    