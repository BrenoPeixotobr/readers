from django import forms

from .models import LivBib


class PostLivBib(forms.ModelForm):
    #biblioteca = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = LivBib
        fields = ('biblioteca','livro')
