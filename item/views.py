from django.shortcuts import render
from django.db.models import Subquery
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Item
from  .forms import PostItem
from livbib.models import LivBib
from usuario.models import Usuario
from django.db.models import Q
from django.shortcuts import render_to_response
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''


def insere_item(request,pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostItem(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostItem()
            livbib=LivBib.objects.filter(idLivBib=pk)
            form.fields["livbib"]=forms.ModelChoiceField(queryset=LivBib.objects.filter(idLivBib=pk),initial={'livbib': pk})
            return render(request, "item/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')


def lista_item(request):
    if request.user.is_authenticated:
        item = Item.objects.all()
        contexto = {
            'item': item
            }
        return render(request, "item/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')
