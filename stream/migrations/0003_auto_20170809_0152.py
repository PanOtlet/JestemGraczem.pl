# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_auto_20170728_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitch',
            name='facebook_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='twitch',
            name='youtube_url',
            field=models.URLField(null=True),
        ),
    ]
