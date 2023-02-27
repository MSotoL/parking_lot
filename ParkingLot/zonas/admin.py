from django.contrib import admin
from .models import Zona

# Register your models here.
class ZonaAdmin(admin.ModelAdmin):
    fields=("id_planta", "descripcion", "observaciones", "created", "updated")
    readonly_fields=("created", "updated")

admin.site.register(Zona, ZonaAdmin)