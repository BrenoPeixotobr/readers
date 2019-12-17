from django.shortcuts import render
from django.db.models import Subquery
from django.shortcuts import get_list_or_404, get_object_or_404
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Emprestimo
from  .forms import PostEmprestimo, PostEntrega
from biblioteca.models import Biblioteca
from usuario.models import Usuario
from livro.models import Livro
from livbib.models import LivBib
from item.models import Item
from item.models import Item
from django.db.models import Q
from django.shortcuts import render_to_response
import dateutil.parser

def emprestar(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostEmprestimo(request.POST)
            if form.is_valid():
                user=Usuario.objects.filter(CPF=form['leitor'].value()).values('user_id')
                c=str(user)
                c2=c.split(': ')
                c3=c2[1].split("}")
                user = get_object_or_404(User, pk=c3[0])
                autorizado = authenticate(username=user,password=form['password'].value())
                print(form['item'].value())
                if autorizado:
                    post = form.save(commit=False)
                    Item.objects.filter(idItem=id).update(status="E")
                    liv=Item.objects.filter(idItem=id).values("livbib")
                    c=str(liv)
                    c2=c.split(': ')
                    c3=c2[1].split("}")
                    livbib=c3[0]
                    post.save()
                    return HttpResponseRedirect('../../item/lista/'+livbib)
                else:
                    mensagem_de_erro="Leitor ou senha invalidos!"
                    contexto = {
                        'mensagem_de_erro': mensagem_de_erro
                        }
                    return render(request, "emprestimo/erros.html", contexto)
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostEmprestimo()
            form.fields["item"]=forms.ModelChoiceField(queryset=Item.objects.filter(idItem=id),initial={'item':id})
            form.fields["bibliotecario"]=forms.ModelChoiceField(queryset=Usuario.objects.filter(user=request.user.id))
            return render(request, "emprestimo/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')

def devolver(request,id,item):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostEntrega(request.POST)
            if form.is_valid():
                Emprestimo.objects.filter(idEmprestimo=id).update(dataEntrega=dateutil.parser.parse(form['data'].value()))
                Item.objects.filter(idItem=item).update(status="L")
                liv=Item.objects.filter(idItem=item).values("livbib")
                c=str(liv)
                c2=c.split(': ')
                c3=c2[1].split("}")
                livbib=c3[0]
                return HttpResponseRedirect('../../devolver_emprestimo/'+str(id))
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostEntrega()
            return render(request, "emprestimo/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')

def lista_emprestimo(request,biblioteca):
    if request.user.is_authenticated:
        livbib=LivBib.objects.filter(biblioteca=biblioteca)
        itens=Item.objects.filter(livbib__in=livbib)
        emprestimo = Emprestimo.objects.filter(item__in=itens).order_by('dataEmprestimo').reverse()
        contexto = {
            'emprestimo': emprestimo
            }
        return render(request, "emprestimo/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')

def devolver_emprestimo(request,id):
    if request.user.is_authenticated:
        emprestimo = Emprestimo.objects.filter(idEmprestimo=id)
        contexto = {
            'emprestimo': emprestimo
            }
        return render(request, "emprestimo/devolver.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')





# Create your views here.
