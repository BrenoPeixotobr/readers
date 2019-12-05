from django import forms

from .models import LivBib


class PostLivBib(forms.ModelForm):
    quantidade = forms.IntegerField(label='Quantidade')
    quantidadeTotal=forms.IntegerField(label='Total')
#    biblioteca = forms.ModelMultipleChoiceField(queryset=Biblioteca.objects.filter(user=request.user.id))
    class Meta:
        model = LivBib
        fields = ('quantidade','quantidadeTotal','biblioteca','livro')
