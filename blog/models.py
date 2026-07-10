from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)

    autor = models.CharField(max_length=50,default="Admin")

    conteudo = models.TextField()

    data_publicacao = models.DateTimeField(auto_now_add=True)

    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)

    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"mensagem de {self.nome}"