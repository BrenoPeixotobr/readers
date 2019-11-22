from django.db import models

class Autor(models.Model):
    nome = models.CharField(primary_key=True,max_length=50)
    dataNascimento = models.DateField(null=True)

# Create your models here.
