from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Reserva
from usuario.models import Usuario
from item.models import Item
from livbib.models import LivBib
from  .forms import PostReserva
from django.shortcuts import render_to_response


def insere_reserva(request,id):
    if request.user.is_authenticated:
        bib_user=Usuario.objects.filter(user=request.user)
        item=Item.objects.filter(idItem=id)
        Item.objects.filter(idItem=id).update(status="R")
        reserva = Reserva.objects.create(item=item[0],leitor=bib_user[0])
        reserva.save()
        mensagem_de_erro="Reserva Feita!"
        contexto = {
            'mensagem_de_erro': mensagem_de_erro
            }
        return render(request, "reserva/erros.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')

def lista_reserva(request,biblioteca):
    if request.user.is_authenticated:
        livbib=LivBib.objects.filter(biblioteca=biblioteca)
        itens=Item.objects.filter(livbib__in=livbib)
        reserva = Reserva.objects.filter(item__in=itens).order_by('dataExpira')

        contexto = {
            'reserva': reserva
            }
        return render(request, "reserva/lista.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')

def cancela(request,id):
    if request.user.is_authenticated:
        item=Reserva.objects.filter(idReserva=id).values("item")
        c=str(item)
        c2=c.split(': ')
        c3=c2[1].split("}")
        item=c3[0]
        Item.objects.filter(idItem=item).update(status="L")
        mensagem_de_erro="Cancelamento Feito"
        contexto = {
            'mensagem_de_erro': mensagem_de_erro
            }
        return render(request, "reserva/erros.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')


# Create your views here.
