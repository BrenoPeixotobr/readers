# Generated by Django 2.2.6 on 2019-11-22 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_livro_autor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autores',
        ),
    ]
