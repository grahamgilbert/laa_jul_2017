# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20170709_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='status',
            field=models.CharField(choices=[('Stock', 'Stock'), ('Deployed', 'Deployed'), ('Lost / Stolen', 'Lost / Stolen')], default='Stock', max_length=200),
        ),
    ]
