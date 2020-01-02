from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('inserir/<int:id>', views.insere_reserva, name='insere_reserva'),
    path('lista/<str:biblioteca>', views.lista_reserva, name='lista_reserva'),
    path('cancela/<int:id>', views.cancela, name='cancela'),

]
