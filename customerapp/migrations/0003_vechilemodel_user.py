# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customerapp', '0002_auto_20181016_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='vechilemodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
