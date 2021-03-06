# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0015_auto_20170824_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='feed_number',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='fish_length',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='fish_number',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='fish_weight',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='fish_width',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]
