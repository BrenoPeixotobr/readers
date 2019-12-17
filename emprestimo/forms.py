from django import forms

from .models import Emprestimo
from datetime import datetime,  timedelta

class PostEmprestimo(forms.ModelForm):
    #leitor = forms.CharField(label='Leitor')
    #dataEmprestimo = forms.DateTimeField(label='Data de Emprestimo')
    #dataPreDev = forms.DateTimeField(label='Data de Entrega')
    password=forms.CharField(widget=forms.PasswordInput)
    #item=forms.IntegerField(label="Livro",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #bibliotecario=forms.CharField(label='Bibliotecario',widget=forms.TextInput(attrs={'readonly':'readonly'}))


    class Meta:
        model = Emprestimo
        fields = ('leitor','item','bibliotecario')

class PostEntrega(forms.Form):
    data=forms.DateTimeField(label='Data da Devolução',input_formats=['%d/%m/%Y'],widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))
