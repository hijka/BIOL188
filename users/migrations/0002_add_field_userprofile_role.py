# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[(b'teacher', b'Teacher'), (b'mentor', b'Mentor'), (b'student', b'Student')], default=b'student', max_length=15),
        ),
    ]
