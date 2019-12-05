from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('inserir/', views.insere_livro, name='insere_livro'),
    path('lista/', views.lista_livro, name='lista_livro'),

]
