# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_add_field_classroom_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]