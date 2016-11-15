# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_auto_20161026_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logger',
            name='server',
        ),
        migrations.AddField(
            model_name='logger',
            name='server',
            field=models.ManyToManyField(null=True, to='cmdb.Server'),
        ),
    ]
