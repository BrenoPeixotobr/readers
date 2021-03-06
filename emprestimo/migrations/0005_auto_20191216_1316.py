# Generated by Django 2.2.6 on 2019-12-16 13:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20191212_1711'),
        ('emprestimo', '0004_auto_20191212_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='biblioteca',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='livro',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='item.Item'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataEmprestimo',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 16, 13, 16, 37, 119029)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataPreDev',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 23, 13, 16, 37, 119067)),
        ),
    ]
