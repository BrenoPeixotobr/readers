from django import forms

from .models import Biblioteca

class PostBiblioteca(forms.ModelForm):
    nome=forms.CharField(label='Nome')
    rua = forms.CharField(label='Rua')
    numero = forms.IntegerField(label='Número')
    complemento = forms.CharField(label='Complemento')
    bairro = forms.CharField(label='Bairro')
    cidade = forms.CharField(label='Cidade')
    estado = forms.CharField(label='Estado')
    pais = forms.CharField(label='País')
    cep = forms.CharField(label='CEP')
    email= forms.CharField(label='Email')
    telefone = forms.CharField(label='Telefone')

    class Meta:
        model = Biblioteca
        fields = ('nome', 'rua','numero','complemento','bairro','cidade','estado','pais','cep','email','telefone','usuario')
