# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='phone_number',
        ),
    ]
