# Generated by Django 2.2.6 on 2019-12-12 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_auto_20191212_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='dataExpira',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 19, 14, 7, 33, 665031)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='dataReserva',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 12, 14, 7, 33, 665003)),
        ),
    ]