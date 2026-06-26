from django.http import HttpResponse

def home(request):
    mensagem = "<h1>bem-vindo ao DevBlog</h1> <p>Em breve arquivos aqui.</p>"

    return HttpResponse(mensagem)

def sobre(request):
    mensagem = "<h1><strong>Sobre o DevBlog</strong></h1> <p><em>testes <br>gostosos</em> 😍</p> "

    return HttpResponse(mensagem)