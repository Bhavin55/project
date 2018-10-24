# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 17:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_address', models.CharField(max_length=20)),
                ('cus_nation', models.CharField(max_length=20)),
                ('cus_phone', models.IntegerField(default=10)),
                ('cus_gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=20)),
                ('created_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]