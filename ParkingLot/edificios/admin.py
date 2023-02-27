from django.contrib import admin
from .models import Edificio

# Register your models here.
class EdificioAdmin(admin.ModelAdmin):
    fields=("id_parking", "descripcion", "observaciones","created", "updated")
    readonly_fields=("created", "updated")

admin.site.register(Edificio, EdificioAdmin)