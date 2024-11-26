from django.db import models
from django.contrib.auth.models import User

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Publicação de {self.usuario.username} em {self.data_publicacao}"
