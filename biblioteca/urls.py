from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('inserir/', views.insere_biblioteca, name='insere_biblioteca'),
    path('lista/', views.lista_biblioteca, name='lista_biblioteca'),
    path('atualiza/<str:nome>', views.atualiza, name='atualiza'),
    path('atualiza/', views.atualiza, name='atualiza'),
    path('minhas_biblioteca/', views.minhas_biblioteca, name='minhas_biblioteca'),
    path('lista_livros/<str:nome>', views.lista_livros, name='lista_livros'),

]
