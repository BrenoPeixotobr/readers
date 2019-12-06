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
            form = PostLivBib()
            bib_user=Usuario.objects.filter(user=request.user)
            form.fields["biblioteca"]=forms.ModelMultipleChoiceField(queryset=Biblioteca.objects.filter(usuario=bib_user[0]))
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
        print(lista_biblioteca[0])
        liv = LivBib.objects.filter(biblioteca=lista_biblioteca[0])
        contexto = {
            'liv': liv
            }
        return render(request, "livbib/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')
# Create your views here.
