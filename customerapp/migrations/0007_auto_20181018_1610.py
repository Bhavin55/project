# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0006_auto_20181018_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vechilemodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='vechilemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
