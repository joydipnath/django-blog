# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20181009_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='key_words',
            field=models.CharField(max_length=100),
        ),
    ]
