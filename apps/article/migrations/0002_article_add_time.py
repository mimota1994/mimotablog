# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-19 19:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]
