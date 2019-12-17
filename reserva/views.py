from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Reserva
from usuario.models import Usuario
from  .forms import PostReserva
from django.shortcuts import render_to_response


def insere_reserva(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostReserva(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
            else:
                return render_to_response("erros/erro_form.html",{'form': form})
        else:
            form = PostReserva()
            form.fields["autor"]=forms.ModelMultipleChoiceField(queryset=Autor.objects.all(),widget=forms.CheckboxSelectMultiple)
            return render(request, "livro/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login/')


# Create your views here.
