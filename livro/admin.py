from django.contrib import admin
from .models import Livro
from .models import Autores

admin.site.register(Autores)
admin.site.register(Livro)


# Register your models here.
