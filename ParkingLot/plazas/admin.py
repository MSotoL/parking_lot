from django.contrib import admin
from .models import Plaza

# Register your models here.
class PlazaAdmin(admin.ModelAdmin):
    fields=("id_zona", "descripcion", "observaciones", "id_tipo_plaza", "created", "updated")
    readonly_fields=("created", "updated")

admin.site.register(Plaza, PlazaAdmin)