from django import forms

from .models import Autor

class PostAutor(forms.ModelForm):
    nome = forms.CharField(label='Nome completo')
    dataNas = forms.DateField(label='Data Nascimento',widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    class Meta:
        model = Autor
        fields = ('nome','dataNas')
