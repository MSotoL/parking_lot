from django.contrib import admin
from .models import Parking

# Register your models here.
class ParkingAdmin(admin.ModelAdmin):
    fields=("descripcion","ubicacion", "observaciones","created", "updated")
    readonly_fields=("created", "updated")

admin.site.register(Parking, ParkingAdmin)
