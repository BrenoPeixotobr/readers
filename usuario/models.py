from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    TIPO_CHOICES = (
       ("L", "Leitor"),
       ("D", "Dono"),
       ("B", "Bibliotecário")

    )

    cpf = models.CharField(primary_key=True,max_length=16)
    nome = models.CharField(max_length=30)
    rua = models.CharField(null=False,max_length=30)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(null=False,max_length=30)
    bairro = models.CharField(null=False,max_length=30)
    cidade = models.CharField(null=False,max_length=30)
    pais = models.CharField(null=False,max_length=30)
    cep = models.CharField(null=False,max_length=30)
    email= models.CharField(null=False,max_length=30)
    telefone = models.CharField(null=False,max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False,default='L')

    def __str__(self):
        return self.nome


# Create your models here.
