# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
