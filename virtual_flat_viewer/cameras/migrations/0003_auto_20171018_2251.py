# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0002_auto_20171016_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='position_left',
            field=models.CharField(default='0', max_length=128),
        ),
        migrations.AlterField(
            model_name='camera',
            name='position_top',
            field=models.CharField(default='0', max_length=128),
        ),
    ]
