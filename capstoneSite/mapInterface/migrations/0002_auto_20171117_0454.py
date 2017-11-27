# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-11-17 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapInterface', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='profile',
            name='distance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
