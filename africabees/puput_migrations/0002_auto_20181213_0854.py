# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 08:54
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('puput', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blogpage',
            managers=[
                ('extra', django.db.models.manager.Manager()),
            ],
        ),
    ]
