from django import forms

from .models import Emprestimo

class PostEmprestimo(forms.ModelForm):
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
    dataEntrega = forms.DateField(label='Data Entrega',input_formats=['%d/%m/%Y'],widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))


    class Meta:
        model = Emprestimo
        fields = ('nome', 'rua','numero','complemento','bairro','cidade','estado','pais','cep','email','telefone','usuario')
