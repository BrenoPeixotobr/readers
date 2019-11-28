# Generated by Django 2.2.6 on 2019-11-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_usuario_complemento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_active',
            new_name='ativado',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='is_staff',
            new_name='equipe',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='is_trusty',
            new_name='validado',
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(default='Minas Gerais', max_length=30),
        ),
    ]