# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='serial',
            field=models.CharField(default='abc123', max_length=200),
            preserve_default=False,
        ),
    ]
