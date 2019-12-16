from django import forms

from .models import Item

class PostItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('livbib', 'status','estado')
