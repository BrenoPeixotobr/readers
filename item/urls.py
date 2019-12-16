from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('inserir/<int:pk>', views.insere_item, name='insere_item'),
    path('lista/<int:liv>', views.lista_item, name='lista_item'),
    path('lista_nome/<str:nome>', views.lista_item_biblioteca, name='lista_item_biblioteca'),


]
