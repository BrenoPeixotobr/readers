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

    CPF=forms.CharField(label='CPF')
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
    tipo = forms.ChoiceField(choices=TIPO_CHOICES,label='Função',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    user = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Usuario
        fields = ('CPF','nome', 'rua','numero','complemento','bairro','cidade','estado','pais','cep','email','telefone','sexo','tipo','user')

class BuscaLivro(forms.Form):
    livro=forms.CharField(label='Titulo', required=False)
    autor=forms.CharField(label='Nome do Autor', required=False)

class PrimeiroLogin(forms.ModelForm):
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

    CPF=forms.CharField(label='CPF')
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
    tipo = forms.ChoiceField(choices=TIPO_CHOICES,label='Função',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    user = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Usuario
        fields = ('CPF','nome', 'rua','numero','complemento','bairro','cidade','estado','pais','cep','email','telefone','sexo','tipo','user')
