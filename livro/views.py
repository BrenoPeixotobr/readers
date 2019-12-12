from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Livro
from autor.models import Autor
from  .forms import PostLivro
from django.shortcuts import render_to_response
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''


def insere_livro(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostLivro(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostLivro()
            return render(request, "livro/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')


def lista_livro(request):
    if request.user.is_authenticated:
        livro = Livro.objects.all()
        contexto = {
            'livro': livro
            }
        return render(request, "livro/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')


def busca_autor(request,autor):
    if request.user.is_authenticated:
        livro = Livro.objects.filter(autor=autor)
        if livro:
            contexto = {
                'livro': livro
                }
            return render(request, "livro/lista.html", contexto)
        else:
            mensagem_de_erro="Não existe livros com esse autor!"
            contexto = {
                'mensagem_de_erro': mensagem_de_erro
                }
            return render(request, "livro/erros.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')
# Create your views here.
