from django.db import models
from autor.models import Autor

class Livro(models.Model):
    isbn =  models.CharField(primary_key=True,max_length=30)
    titulo = models.CharField(max_length=50, blank=False)
    area = models.CharField(max_length=50, blank=False)
    subarea = models.CharField(max_length=50, blank=False)
    anoPublicacao = models.CharField(max_length=50, blank=False)
    editora = models.CharField(max_length=50, blank=False)
    edicao = models.IntegerField(null=True)
    autor = models.ManyToManyField(Autor)


    def __str__(self):
        return self.titulo
# Create your models here.
