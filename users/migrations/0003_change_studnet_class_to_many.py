# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_add_field_userprofile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ManyToManyField(related_name='students', to='users.Classroom'),
        ),
    ]
