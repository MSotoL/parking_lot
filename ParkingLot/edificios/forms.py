from django import forms
from .models import Edificio
 
class form_crear_parking(forms.ModelForm):
    class Meta:
        model = Edificio
        descripcion=forms.CharField(label="Descripción",max_length=50,required=True)
        observaciones=forms.CharField(label="Observaciones", widget=forms.Textarea)
        id_parking=forms.forms.IntegerField(label="Parking", required=True)