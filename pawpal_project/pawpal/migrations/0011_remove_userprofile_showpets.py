# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawpal', '0010_auto_20180321_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='showPets',
        ),
    ]
