from django.shortcuts import render
from django.db.models import Subquery
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import LivBib
from  .forms import PostLivBib
from biblioteca.models import Biblioteca
from usuario.models import Usuario
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
            print(bib_user[0])
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
# Create your views here.
