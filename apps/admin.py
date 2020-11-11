from django.contrib import admin
from .models import Compañia, Juego, Contacto
# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio" , "Compañia"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["Compañia" , "precio"]
    list_per_page = 5


admin.site.register(Compañia)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Contacto)
