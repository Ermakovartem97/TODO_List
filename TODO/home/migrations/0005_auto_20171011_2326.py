# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171011_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_active',
            field=models.BooleanField(default=None),
        ),
    ]
