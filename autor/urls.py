from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('inserir/', views.insere_autor, name='insere_autor'),
    path('lista/', views.lista_autor, name='lista_autor'),
    path('busca/', views.busca_autor, name='busca_autor'),

]
