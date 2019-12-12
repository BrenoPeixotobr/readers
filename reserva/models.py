from django.db import models
from usuario.models import Usuario
from livro.models import Livro
from biblioteca.models import Biblioteca
from datetime import datetime,  timedelta


class Reserva(models.Model):
    idReserva=models.AutoField(primary_key=True)
    leitor = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='Reserva_leitor')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    dataReserva = models.DateTimeField(default=datetime.now(), blank=True)
    dataExpira = models.DateTimeField(default=datetime.now() + timedelta(days=7), blank=True)

    def __str__(self):
        return str(self.livro)



# Create your models here.
