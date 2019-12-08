from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Usuario
from  .forms import PostUsuario, BuscaLivro, PrimeiroLogin
from django.shortcuts import render_to_response
from django.db.models import Q
'''
def post_list(request):
    if request.user.is_authenticated:

    else:
        return HttpResponseRedirect('../login/')
'''

def post_list(request):
    if request.user.is_authenticated:
        user=request.user.id
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
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            user_id=request.user.id
            form = PostUsuario(initial={'user': user_id,'tipo':"Leitor"})
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
        user_logado=Usuario.objects.filter(user=request.user.id)
        if not user_logado:
            if request.method == "POST":
                form = PrimeiroLogin(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
                    return HttpResponseRedirect('../lista/')
                else:
                    return render_to_response("erros/erro_form.html",{'form': form})
            else:
                nome_usuario=request.user
                user_id=request.user.id
                form = PrimeiroLogin(initial={'user': user_id,'tipo':"L"})
                return render(request, "usuario/primeiro.html",{'form': form,'nome_usuario': nome_usuario})

        else:
            return HttpResponseRedirect('../busca/')

    else:
        return HttpResponseRedirect('../login/')

def atualiza_dados(request):
    if request.user.is_authenticated:
        post = get_object_or_404(Usuario, user=request.user.id)
        form = PostUsuario(instance=post)
        if(request.method == 'POST'):
            form = PostUsuario(request.POST, instance=post)
            Usuario.objects.filter(user=request.user.id).update(CPF=form['CPF'].value())
            Usuario.objects.filter(user=request.user.id).update(nome=form['nome'].value())
            Usuario.objects.filter(user=request.user.id).update(rua=form['rua'].value())
            Usuario.objects.filter(user=request.user.id).update(numero=form['numero'].value())
            Usuario.objects.filter(user=request.user.id).update(complemento=form['complemento'].value())
            Usuario.objects.filter(user=request.user.id).update(bairro=form['bairro'].value())
            Usuario.objects.filter(user=request.user.id).update(cidade=form['cidade'].value())
            Usuario.objects.filter(user=request.user.id).update(estado=form['estado'].value())
            Usuario.objects.filter(user=request.user.id).update(cep=form['cep'].value())
            Usuario.objects.filter(user=request.user.id).update(email=form['email'].value())
            Usuario.objects.filter(user=request.user.id).update(telefone=form['telefone'].value())
            Usuario.objects.filter(user=request.user.id).update(sexo=form['sexo'].value())
            return HttpResponseRedirect('../lista/')


        elif(request.method == 'GET'):
            return render(request, 'usuario/edit_usuario.html', {'form': form, 'post' : post})

    else:
        return HttpResponseRedirect('../login/')

# Create your views here.
