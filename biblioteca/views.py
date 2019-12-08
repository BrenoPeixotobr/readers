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

def atualiza(request):
    if request.user.is_authenticated:
        post = get_object_or_404(Biblioteca, user=request.biblioteca.id)
        form = PostBiblioteca(instance=post)
        if(request.method == 'POST'):
            form = PostBiblioteca(request.POST, instance=post)
            Biblioteca.objects.filter(userio=request.user.id).update(nome=form['nome'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(rua=form['rua'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(numero=form['numero'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(complemento=form['complemento'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(bairro=form['bairro'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(cidade=form['cidade'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(estado=form['estado'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(cep=form['cep'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(email=form['email'].value())
            Biblioteca.objects.filter(userio=request.user.id).update(telefone=form['telefone'].value())
            #Biblioteca.objects.filter(userio=request.user.id).update(Usuario.objects.filter(user=request.user)) 
            return HttpResponseRedirect('../lista/')


        elif(request.method == 'GET'):
            return render(request, 'biblioteca/edit_biblioteca.html', {'form': form, 'post' : post})

    else:
        return HttpResponseRedirect('../login/')
# Create your views here.
