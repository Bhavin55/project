# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 13:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customerapp', '0008_auto_20181018_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ve_type', models.CharField(max_length=20)),
                ('Ve_accomadate', models.IntegerField(default=0)),
                ('Ve_model', models.IntegerField(default=0)),
                ('Ve_price', models.IntegerField(default=0)),
                ('Ve_photo', models.ImageField(upload_to='media/pic/')),
                ('Ve_file', models.FileField(upload_to='media/file/')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default='user.username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='vechilemodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='VechileModel',
        ),
    ]