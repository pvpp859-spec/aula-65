from django.contrib import admin
from .models import Categoria, Artigo

# Register your models here.

admin.site.register(Categoria)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'Categoria', 'data_publicacao')
    
    search_fields = ('titulo', 'conteudo')
    
    list_filter = ('Categoria', 'data_publicacao')

from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'senha123')
