# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-11 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='location',
            field=models.CharField(default='Glasgow', max_length=30),
        ),
    ]
