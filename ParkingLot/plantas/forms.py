from django import forms
from .models import Planta
 
class form_crear_parking(forms.ModelForm):
    class Meta:
        model = Planta
        descripcion=forms.CharField(label="Descripción",max_length=50,required=True)
        max_plazas=forms.IntegerField(label="Nº Máximo de Plazas", required=True)
        observaciones=forms.CharField(label="Observaciones", widget=forms.Textarea)
        id_parking=forms.forms.IntegerField(label="Parking", required=True)