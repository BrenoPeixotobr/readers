from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Usuario
from  .forms import PostUsuario
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''

def post_list(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../inserir/')
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
            form = PostUsuario()
            return render(request, "usuario/inserir.html",{'form': form})
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

# Create your views here.
