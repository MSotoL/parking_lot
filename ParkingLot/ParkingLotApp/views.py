from django.shortcuts import render, HttpResponse

# Create your views here.

# Vista de la página inicial
def home(request):
    
    #return HttpResponse("Home")
    
    return render(request, "ParkingLotApp/home.html")