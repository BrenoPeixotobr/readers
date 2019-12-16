from django.db import models
from biblioteca.models import Biblioteca
from usuario.models import Usuario

class UserBib(models.Model):
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.usuario)


# Create your models here.
