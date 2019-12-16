from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('inserir/', views.insere_livbib, name='insere_livbib'),
    path('lista/', views.lista_livbib, name='lista_livbib'),
    path('lista_cidade_user/<str:livro>', views.lista_cidade_biblioteca, name='lista_cidade_biblioteca'),
    path('lista_livro/<str:livro>', views.lista_livro, name='lista_livro'),
    path('inserir_bib/<str:biblioteca>', views.insere_bib, name='insere_bib'),
    path('lista_livros_biblioteca/<str:nome>', views.lista_livros_biblioteca, name='lista_livros_biblioteca'),

]
