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



# Create your views here.
