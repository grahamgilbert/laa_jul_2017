# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20170709_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='windows_vm',
            field=models.BooleanField(default=False, verbose_name='Assign a Windows VM'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='status',
            field=models.CharField(choices=[('Stock', 'Stock'), ('Deployed', 'Deployed'), ('High Risk Location', 'High Risk Location'), ('Lost / Stolen', 'Lost / Stolen')], default='Stock', max_length=200),
        ),
    ]
