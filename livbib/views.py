from django.shortcuts import render
from django.db.models import Subquery
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import LivBib
from  .forms import PostLivBib
from biblioteca.models import Biblioteca
from usuario.models import Usuario
from livro.models import Livro
from django.db.models import Q
from django.shortcuts import render_to_response
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''


def insere_livbib(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostLivBib(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostLivBib()
            bib_user=Usuario.objects.filter(user=request.user)
            form.fields["biblioteca"]=forms.ModelChoiceField(queryset=Biblioteca.objects.filter(usuario=bib_user[0]))
            return render(request, "livbib/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')


def lista_livbib(request):
    if request.user.is_authenticated:
        liv = LivBib.objects.all()

        contexto = {
            'liv': liv
            }
        return render(request, "livbib/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')

def lista_cidade_biblioteca(request,livro):
    if request.user.is_authenticated:
        #usuario corrente
        bib_user=Usuario.objects.filter(user=request.user).values("cidade")
        c=str(bib_user)
        c2=c.split(':')
        c3=c2[1].split("'")
        cidade=c3[1]
        #id do livro pesquisado
        id_livro=Livro.objects.filter(titulo=livro)
        lista_biblioteca=Biblioteca.objects.filter(cidade=cidade)
        liv = LivBib.objects.filter(Q(biblioteca__in=lista_biblioteca) & Q(livro=id_livro[0]))
        if liv:
            contexto = {
                'liv': liv
                }
            return render(request, "livbib/lista.html", contexto)
        else:
            mensagem_de_erro="Não existe esse livro na sua cidade!"
            contexto = {
                'mensagem_de_erro': mensagem_de_erro
                }
            return render(request, "livbib/erros.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')
# Create your views here.

def lista_livro(request,livro):
    if request.user.is_authenticated:
        id_livro=Livro.objects.filter(titulo=livro)
        liv = LivBib.objects.filter(livro=id_livro[0])
        contexto = {
            'liv': liv
                    }
        return render(request, "livbib/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')

def insere_bib(request,biblioteca):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostLivBib(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostLivBib()
            bib_user=Usuario.objects.filter(user=request.user)
            form.fields["biblioteca"]=forms.ModelChoiceField(queryset=Biblioteca.objects.filter(Q(usuario=bib_user[0]) & Q(nome=biblioteca)),initial=biblioteca)
            #form.fields["biblioteca"]=biblioteca
            return render(request, "livbib/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')
