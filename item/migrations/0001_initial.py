# Generated by Django 2.2.6 on 2019-12-12 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livbib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('idItem', models.AutoField(primary_key=True, serialize=False)),
                ('staus', models.CharField(choices=[('L', 'Livre'), ('R', 'Reservado'), ('E', 'Emprestado')], default='L', max_length=1)),
                ('estado', models.CharField(choices=[('N', 'Novo'), ('C', 'Conservado'), ('R', 'Ruim')], default='L', max_length=1)),
                ('livbib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livbib.LivBib')),
            ],
        ),
    ]
