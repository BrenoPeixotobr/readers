from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('emprestar/<int:id>', views.emprestar, name='emprestar'),
    path('devolver/<int:id>', views.devolver, name='devolver'),

]
