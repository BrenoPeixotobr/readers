from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Biblioteca
from  .forms import PostBiblioteca
from django.shortcuts import render_to_response
from usuario.models import Usuario
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''


def insere_biblioteca(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostBiblioteca(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                Usuario.objects.filter(user=request.user.id).update(tipo="D")
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostBiblioteca(initial = {'usuario': request.user.id })
            bib_user=Usuario.objects.filter(user=request.user)
            form.fields['usuario']=forms.ModelChoiceField(queryset=Usuario.objects.filter(user=request.user),initial=bib_user[0])
            return render(request, "biblioteca/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')


def lista_biblioteca(request):
    if request.user.is_authenticated:
        biblioteca = Biblioteca.objects.all()
        contexto = {
            'biblioteca': biblioteca
            }
        return render(request, "biblioteca/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')


def minhas_biblioteca(request):
    if request.user.is_authenticated:
        bib_user=Usuario.objects.filter(user=request.user)
        biblioteca = Biblioteca.objects.filter(usuario__in=bib_user)
        if biblioteca:
            contexto = {
                'biblioteca': biblioteca
                }
            return render(request, "biblioteca/lista_minha_bib.html", contexto)
        else:
            mensagem_de_erro="Não biblioteca para esse usuario"
            contexto = {
                'mensagem_de_erro': mensagem_de_erro
                }
            return render(request, "biblioteca/erros.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')
# Create your views here.
