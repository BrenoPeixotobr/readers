from django import forms

from .models import Autor

class PostAutor(forms.ModelForm):
    nome = forms.CharField(label='Nome completo')
    dataNascimento = forms.DateField(label='Data Nascimento',input_formats=['%d/%m/%Y'],widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))
    class Meta:
        model = Autor
        fields = ('nome','dataNascimento')

class BuscaAutor(forms.Form):
    autor=forms.CharField(label='Nome do Autor')
