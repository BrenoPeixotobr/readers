from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=("User"))
    CPF = models.CharField(primary_key=True,max_length=30)
    nome = models.CharField(max_length=30)
    rua = models.CharField(null=False,max_length=30)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(null=False,max_length=30)
    bairro = models.CharField(null=False,max_length=30)
    cidade = models.CharField(null=False,max_length=30)
    estado = models.CharField(null=False,max_length=30,default="Minas Gerais")
    pais = models.CharField(null=False,max_length=30)
    cep = models.CharField(null=False,max_length=30)
    email= models.CharField(null=False,max_length=30)
    telefone = models.CharField(null=False,max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False,default='L')

    def __str__(self):
        return self.nome


    '''
    @receiver(post_save, sender=User)
    def criar_usuario(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def salvar_usuario(sender, instance, **kwargs):
        instance.usuario.save()

'''
# Create your models here.
