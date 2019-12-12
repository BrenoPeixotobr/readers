# Generated by Django 2.2.6 on 2019-12-12 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biblioteca', '0001_initial'),
        ('usuario', '0001_initial'),
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False)),
                ('dataReserva', models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 12, 13, 59, 1, 634926))),
                ('dataExpira', models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 19, 13, 59, 1, 634953))),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Biblioteca')),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserva_leitor', to='usuario.Usuario')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.Livro')),
            ],
        ),
    ]
