from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada',)
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'usuario',)
    list_editable = ('publicada',)
    ordering = ('id',)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografia)
