from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('inserir/', views.insere_livbib, name='insere_livbib'),
    path('lista/', views.lista_livbib, name='lista_livbib'),

]
