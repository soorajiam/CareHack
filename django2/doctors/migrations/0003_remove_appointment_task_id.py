# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_remove_appointment_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='task_id',
        ),
    ]
