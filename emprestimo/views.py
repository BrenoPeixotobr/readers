from django.shortcuts import render
from django.db.models import Subquery
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Emprestimo
from  .forms import PostEmprestimo, PostEntrega
from biblioteca.models import Biblioteca
from usuario.models import Usuario
from livro.models import Livro
from livbib.models import LivBib
from item.models import Item
from item.models import Item
from django.db.models import Q
from django.shortcuts import render_to_response
import dateutil.parser

def emprestar(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostEmprestimo(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                Item.objects.filter(idItem=id).update(status="E")
                liv=Item.objects.filter(idItem=id).values("livbib")
                c=str(liv)
                c2=c.split(': ')
                c3=c2[1].split("}")
                livbib=c3[0]
                post.save()
                return HttpResponseRedirect('../../item/lista/'+livbib)
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostEmprestimo()
            form.fields["item"]=forms.ModelChoiceField(queryset=Item.objects.filter(idItem=id),initial={'item':id})
            form.fields["bibliotecario"]=forms.ModelChoiceField(queryset=Usuario.objects.filter(user=request.user.id))
            return render(request, "emprestimo/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')

def devolver(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostEntrega(request.POST)
            if form.is_valid():
                Emprestimo.objects.filter(item=id).update(dataEntrega=dateutil.parser.parse(form['data'].value()))
                Item.objects.filter(idItem=id).update(status="L")
                liv=Item.objects.filter(idItem=id).values("livbib")
                c=str(liv)
                c2=c.split(': ')
                c3=c2[1].split("}")
                livbib=c3[0]
                return HttpResponseRedirect('../../item/lista/'+livbib)
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostEntrega()
            return render(request, "emprestimo/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')



# Create your views here.
