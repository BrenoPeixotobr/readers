from django.db import models
from biblioteca.models import Biblioteca
from livro.models import Livro

class LivBib(models.Model):
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False)
    quantidadeTotal=models.IntegerField(null=False)


    def __str__(self):
        return str(self.livro)

# Create your models here.
