from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Usuario
from  .forms import PostUsuario, BuscaLivro
from django.shortcuts import render_to_response
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''

def post_list(request):
    if request.user.is_authenticated:
        user=request.user.id
        print(user)
        return render(request, "usuario/teste.html")#return HttpResponseRedirect('../inserir/')
    else:
        return HttpResponseRedirect('../../login/')

def insere_usuario(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostUsuario(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erro_form.html",{'form': form})
        else:
            user_id=request.user.id
            form = PostUsuario(initial={'user': user_id})
            return render(request, "usuario/inserir.html",{'form': form, 'user':user_id})
    else:
        return HttpResponseRedirect('../../login/')


def lista_usuario(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.all()
        contexto = {
            'usuario': usuario
            }
        return render(request, "usuario/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')


def busca_livro(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BuscaLivro(request.POST)
            nome_livro=form['livro'].value()
            return HttpResponseRedirect('../../livbib/lista_cidade_user/'+str(nome_livro))
        else:
            form = BuscaLivro()
            return render(request, "usuario/busca.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')

def primeiro_login(request):
    if request.user.is_authenticated:
        user_logado=Usuario.objects.filter(user=request.user).exist()
        print(user_logado)
        return HttpResponseRedirect('../teste/')

    else:
        return HttpResponseRedirect('../login/')

# Create your views here.
