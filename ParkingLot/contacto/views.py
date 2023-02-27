from django.shortcuts import render, redirect
from .forms import frmContacto
from django.core.mail import EmailMessage

# Create your views here.
# Vista de la página Contacto
def contacto(request):    
    
    formulario_contacto=frmContacto()
    
    if request.method=="POST":
        formulario_contacto=frmContacto(data=request.POST)
        if formulario_contacto.is_valid():            
            nombreContacto=request.POST.get("nombre")
            emailContacto=request.POST.get("email")
            contenidoContacto=request.POST.get("contenido")
            
            email=EmailMessage("Email de contacto desde Gestión de Parkings","Email enviado por {} desde la dirección de correo electrónico {} escribe el siguiente comentario: \n\n {}".format(nombreContacto, emailContacto, contenidoContacto),"",["gestion.parkings.unir@gmail.com"],reply_to=[emailContacto])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?no_valido")
        
    return render(request, "contacto/contacto.html", {"formulario":formulario_contacto})