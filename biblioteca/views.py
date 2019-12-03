from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Biblioteca
from  .forms import PostBiblioteca

def insere_biblioteca(request):
    if request.method == "POST":
        form = PostBiblioteca(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('../lista/')
    else:
        form = PostBiblioteca()
        return render(request, "biblioteca/inserir.html",{'form': form})


def lista_biblioteca(request):
    biblioteca = Biblioteca.objects.all()
    contexto = {
        'biblioteca': biblioteca
        }
    return render(request, "biblioteca/lista.html", contexto)
# Create your views here.
