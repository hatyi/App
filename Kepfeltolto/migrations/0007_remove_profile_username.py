# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kepfeltolto', '0006_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
