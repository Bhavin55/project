# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181013_0406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registermodel',
            old_name='email',
            new_name='user',
        ),
    ]
