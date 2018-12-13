# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-11 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20181211_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='up_vote',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='down_vote',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='up_vote',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='replyoncomment',
            name='down_vote',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='replyoncomment',
            name='up_vote',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
