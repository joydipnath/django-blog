# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-14 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20181214_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='replyoncomment',
            name='comment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='articles.Comment'),
        ),
    ]
