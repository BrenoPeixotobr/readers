from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re
from django.utils import timezone
from django.db import models

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('Nome de usuário inválido.'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, ativado=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.ativado=True
        user.save(using=self._db)
        return user



class Usuario(AbstractBaseUser, PermissionsMixin):
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
    username = models.CharField(_('username'), max_length=15, unique=True, help_text=_('Requerido. 15 caracteres ou menos. Letras, números e  @/./+/-/_'), validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Insira um nome de usuário válido.'), _('inválido'))],default='teste')
    nome = models.CharField(null=False,max_length=30)
    rua = models.CharField(null=False,max_length=30)
    numero = models.IntegerField(null=False)
    bairro = models.CharField(null=False,max_length=30)
    complemento = models.CharField(null=True,max_length=30)
    estado = models.CharField(null=False,max_length=30,default='Minas Gerais')
    cidade = models.CharField(null=False,max_length=30)
    pais = models.CharField(null=False,max_length=30)
    cep = models.CharField(null=False,max_length=30)
    email= models.EmailField(_('email address'), max_length=255, unique=True)
    telefone = models.CharField(null=False,max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False,default='L')
    ativado = models.BooleanField(_('active'), default=True, help_text=_('Designa se este usuário deveria ser tratado como ativo. Desmarca ele ao invés de excluir contas.'))
    validado = models.BooleanField(_('trusty'), default=False, help_text=_('Designa se este usuário confirmou a sua conta.'))
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designa se o usuário pode logar nesta área de administrador.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome','rua','numero','bairro','cidade','pais','cep']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_short_name(self):
        return self.nome
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def __str__(self):
        return self.nome




# Create your models here.
