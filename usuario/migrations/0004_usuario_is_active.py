# Generated by Django 2.2.6 on 2019-11-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_usuario_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]