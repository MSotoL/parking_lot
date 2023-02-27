from django.contrib import admin
from .models import TipoPlaza

# Register your models here.
class TipoPlazaAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(TipoPlaza, TipoPlazaAdmin)