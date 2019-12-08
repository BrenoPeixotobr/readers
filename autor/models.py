from django.db import models
import datetime

class Autor(models.Model):
    nome = models.CharField(primary_key=True,max_length=50)
    dataNascimento = models.DateField(null=True)

# Create your models here.
