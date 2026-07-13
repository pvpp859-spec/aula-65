from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404,redirect
from .models import Artigo, Categoria
from .forms import ContatoForm
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ArtigoSerializer


def home(request):
    noticias = Artigo.objects.all().order_by('-id')
    busca = request.GET.get('q')

    if busca:
        noticias = noticias.filter(titulo__icontains=busca)

    # Movemos o Paginator para fora do 'if' para garantir que ele sempre exista
    paginator = Paginator(noticias, 5) 
    numero_da_pagina = request.GET.get('page')
    page_obj = paginator.get_page(numero_da_pagina)

    contexto = {
        'lista_artigos': page_obj,
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

def artigo_detalhe(request,id):
    noticia = get_object_or_404(Artigo,id = id)

    contexto = {'artigo':noticia}

    return render(request,'blog/artigo_detalhe.html',contexto)

def fale_conosco(request):
    if request.method == 'POST':
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    
    else:
        formulario = ContatoForm()

    return render(request,'blog/contato.html', {'form': formulario})

@api_view(['GET'])
def api_listar_artigos(request):
    artigos = Artigo.objects.all()
    serializer = ArtigoSerializer(artigos,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigo(request):
    serializer = ArtigoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)