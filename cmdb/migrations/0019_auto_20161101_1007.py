# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0018_servergroup_apps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servergroup',
            name='apps',
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='apps',
            field=models.ManyToManyField(to='cmdb.App'),
        ),
    ]
