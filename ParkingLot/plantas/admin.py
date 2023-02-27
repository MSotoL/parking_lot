from django.contrib import admin
from .models import Planta

# Register your models here.
class PlantaAdmin(admin.ModelAdmin):
    fields=("id_edificio", "descripcion", "max_plazas", "observaciones", "created", "updated")
    readonly_fields=("created", "updated")

admin.site.register(Planta, PlantaAdmin)