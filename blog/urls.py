from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sobre/',views.sobre,name="sobre"),

    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('artigo/<int:id>',views.artigo_detalhe,name='detalhe_artigo'),
    path('api/artigos/',views.api_listar_artigos,name='api_artigos'),
]