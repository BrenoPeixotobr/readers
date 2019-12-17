from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('emprestar/<int:id>', views.emprestar, name='emprestar'),
    path('devolver/<int:id>/<int:item>', views.devolver, name='devolver'),
    path('lista/', views.lista_emprestimo, name='lista_emprestimo'),
    path('devolver_emprestimo/<int:id>', views.devolver_emprestimo, name='devolver_emprestimo'),

]
