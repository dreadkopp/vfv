# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-20 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_house_bild'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='Beschreibung',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]