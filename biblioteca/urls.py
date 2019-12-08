from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('inserir/', views.insere_biblioteca, name='insere_biblioteca'),
    path('lista/', views.lista_biblioteca, name='lista_biblioteca'),
    path('minhas_biblioteca/', views.minhas_biblioteca, name='minhas_biblioteca'),

]
