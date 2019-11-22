# Generated by Django 2.2.6 on 2019-11-22 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biblioteca', '0001_initial'),
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LivBib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('quantidadeTotal', models.IntegerField()),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Biblioteca')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.Livro')),
            ],
        ),
    ]
