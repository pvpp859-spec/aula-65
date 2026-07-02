from django.shortcuts import render,get_object_or_404
from .models import Artigo, Categoria 

def home(request):
    noticias = Artigo.objects.all()
    todas_categorias = Categoria.objects.all() 
    
    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': todas_categorias 
    }
    return render(request, 'blog/index.html', contexto)

# ADICIONE AS CATEGORIAS AQUI TAMBÉM:
def sobre(request):
    todas_categorias = Categoria.objects.all() 
    
    contexto = {
        'lista_categorias': todas_categorias
    }
    return render(request, 'blog/sobre.html', contexto)

def categoria(request, categoria_id):
    # Busca a categoria clicada ou dá erro 404 se ela não existir
    categoria_atual = get_object_or_404(Categoria, id=categoria_id)
    
    # Filtra os artigos que pertencem a essa categoria
    noticias_filtradas = Artigo.objects.filter(Categoria=categoria_atual)
    
    # Busca todas as categorias para a Navbar continuar aparecendo no topo
    todas_categorias = Categoria.objects.all()
    
    contexto = {
        'lista_artigos': noticias_filtradas,
        'lista_categorias': todas_categorias,
        'categoria_selecionada': categoria_atual # Opcional: para usar no título da página
    }
    
    # Usamos o mesmo index.html para reaproveitar o visual dos cards!
    return render(request, 'blog/index.html', contexto)