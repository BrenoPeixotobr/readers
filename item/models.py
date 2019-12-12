from django.db import models
from livbib.models import LivBib
STATUS_CHOICES = (
    ("L", "Livre"),
    ("R", "Reservado"),
    ("E", "Emprestado")
)

ESTADO_CHOICES = (
    ("N", "Novo"),
    ("C", "Conservado"),
    ("R", "Ruim")
)

class Item(models.Model):
    idItem=models.AutoField(primary_key=True)
    livbib = models.ForeignKey(LivBib, on_delete=models.CASCADE)
    staus=models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False,default='L')
    estado=models.CharField(max_length=1, choices=ESTADO_CHOICES, blank=False, null=False,default='L')

    def __str__(self):
        return str(self.idItem)
# Create your models here.
