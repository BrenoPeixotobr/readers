from django.db import models
from usuario.models import Usuario
from item.models import Item
from datetime import datetime,  timedelta


class Emprestimo(models.Model):
    idEmprestimo=models.AutoField(primary_key=True)
    bibliotecario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='bibliotecario')
    leitor = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='leitor')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    dataEmprestimo = models.DateTimeField(default=datetime.now(), blank=True)
    dataPreDev = models.DateTimeField(default=datetime.now() + timedelta(days=7), blank=True)
    dataEntrega = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.idEmprestimo)


# Create your models here.
