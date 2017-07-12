# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170708_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='status',
            field=models.CharField(choices=[('Stock', 'Stock'), ('Deployed', 'Deployed'), ('Lost / Stolen', 'Lost / Stolen')], default='Stock', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machine',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
