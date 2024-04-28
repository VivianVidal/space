from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","foto","publicada",)
    list_display_links = ("id","nome",)
    search_fields = ("nome",)
    list_per_page = 3
    list_editable = ("publicada","legenda",)
    

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)    