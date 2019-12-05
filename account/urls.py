from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.register.as_view(), name='register'),


]
