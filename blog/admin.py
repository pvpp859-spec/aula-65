from django.contrib import admin
from .models import Categoria, Artigo

# Register your models here.

admin.site.register(Categoria)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'Categoria', 'data_publicacao')
    
    search_fields = ('titulo', 'conteudo')
    
    list_filter = ('Categoria', 'data_publicacao')