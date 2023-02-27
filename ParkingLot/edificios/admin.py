from django.contrib import admin
from .models import Edificio

# Register your models here.
class EdificioAdmin(admin.ModelAdmin):
    fields=("descripcion", "observaciones","id_created", "updated")
    readonly_fields=("created", "updated")

admin.site.register(Edificio, EdificioAdmin)