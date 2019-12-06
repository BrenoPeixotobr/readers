from django import forms

from .models import LivBib


class PostLivBib(forms.ModelForm):
    quantidade = forms.IntegerField(label='Quantidade')
    quantidadeTotal=forms.IntegerField(label='Total')
    #biblioteca = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = LivBib
        fields = ('quantidade','quantidadeTotal','biblioteca','livro')
