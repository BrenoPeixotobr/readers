from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.busca_livro, name='busca_livro'),
    path('teste', views.post_list, name='post_list'),
    path('inserir/', views.insere_usuario, name='insere_usuario'),
    path('lista/', views.lista_usuario, name='lista_usuario'),
    path('busca/', views.busca_livro, name='busca_livro'),

]
