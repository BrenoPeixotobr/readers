from django import forms

from .models import Livro
from autor.models import Autor

class PostLivro(forms.ModelForm):
    isbn =  forms.CharField(label='ISBN')
    titulo = forms.CharField(label='Titulo')
    area = forms.CharField(label='Área')
    subarea = forms.CharField(label='Subarea')
    anoPublicacao = forms.CharField(label='Ano de publicação')
    editora = forms.CharField(label='Editora')
    edicao = forms.IntegerField(label='Edição')
    class Meta:
        model = Livro
        fields = ('isbn','titulo', 'area','subarea','anoPublicacao','editora','edicao','autor')
