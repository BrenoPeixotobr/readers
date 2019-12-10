from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Autor
from  .forms import PostAutor, BuscaAutor
from django.shortcuts import render_to_response
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''


def insere_autor(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostAutor(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostAutor()
            return render(request, "autor/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')


def lista_autor(request):
    if request.user.is_authenticated:
        autor = Autor.objects.all()
        contexto = {
            'autor': autor
            }
        return render(request, "autor/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')


def busca_autor(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BuscaAutor(request.POST)
            nome_Autor=form['autor'].value()
            return HttpResponseRedirect('../../livro/busca_autor/'+str(nome_Autor))
        else:
            form = BuscaAutor()
            return render(request, "autor/busca.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')

# Create your views here.
