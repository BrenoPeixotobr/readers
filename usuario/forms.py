from django import forms

from .models import Usuario

class PostUsuario(forms.ModelForm):
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

    cpf=forms.CharField(label='CPF')
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
    sexo = forms.ChoiceField(choices=SEXO_CHOICES,label='Orientação Sexual')
    tipo = forms.ChoiceField(choices=TIPO_CHOICES,label='Função')
    class Meta:
        model = Usuario
        fields = ('cpf','nome', 'rua','numero','complemento','bairro','cidade','estado','pais','cep','email','telefone','sexo','tipo','user')

class BuscaLivro(forms.Form):
    livro=forms.CharField(label='Nome do Livro')
    autor=forms.CharField(label='Nome do Autor')
