# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-16 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='position_left',
            field=models.CharField(default='0', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camera',
            name='position_top',
            field=models.CharField(default='0', max_length=128),
            preserve_default=False,
        ),
    ]
