from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('inserir/', views.insere_livbib, name='insere_livbib'),
    path('lista/', views.lista_livbib, name='lista_livbib'),
    path('lista_cidade_user/<str:livro>', views.lista_cidade_biblioteca, name='lista_cidade_biblioteca'),

]
