# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20161021_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='current_version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
