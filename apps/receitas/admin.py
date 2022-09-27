from atexit import register
from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'tempo_preparo', 'publicada', 'date_receita', 'pessoa')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada', )
    list_per_page = 10

admin.site.register(Receita, ListandoReceitas)