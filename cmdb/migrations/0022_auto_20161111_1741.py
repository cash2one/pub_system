# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0021_auto_20161111_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='war_file',
        ),
        migrations.RemoveField(
            model_name='app',
            name='war_file_path',
        ),
    ]