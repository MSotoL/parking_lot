from django import forms
from .models import Parking
 
class form_crear_parking(forms.ModelForm):
    class Meta:
        model = Parking
        descripcion=forms.CharField(label="Descripción",max_length=50,required=True)
        ubicacion=forms.CharField(label="Ubicacion",max_length=100,required=True)
        num_plazas_grandes=forms.CharField(label="Nº PLazas Grandes", disabled=True)
        num_plazas_peq=forms.CharField(label="Nº PLazas Pequeñas", disabled=True)
        num_plazas_discap=forms.CharField(label="Nº PLazas Minusválidos", disabled=True)
        observaciones=forms.CharField(label="Observaciones", widget=forms.Textarea)