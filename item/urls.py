from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('inserir/<int:pk>', views.insere_item, name='insere_item'),
    path('lista/<int:liv>', views.lista_item, name='lista_item'),


]
