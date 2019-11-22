from django.db import models
from livro.models import Livro
from usuario.models import Usuario
#from livbib.models import LivBib


class Biblioteca(models.Model):
    nome = models.CharField(primary_key=True,max_length=30)
    rua = models.CharField(null=False,max_length=30)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(null=False,max_length=30)
    bairro = models.CharField(null=False,max_length=30)
    cidade = models.CharField(null=False,max_length=30)
    pais = models.CharField(null=False,max_length=30)
    cep = models.CharField(null=False,max_length=30)
    email= models.CharField(null=False,max_length=30)
    telefone = models.CharField(null=False,max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        unique_together = ('nome', 'usuario')


# Create your models here.
