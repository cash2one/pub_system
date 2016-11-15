# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 02:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=30, unique=True)),
                ('upload_path', models.CharField(max_length=100)),
                ('app_path', models.CharField(default=b'release', max_length=100)),
                ('backup_path', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('war_file', models.NullBooleanField()),
                ('war_file_path', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backup_name', models.CharField(max_length=30)),
                ('backup_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, b'Successfull'), (1, b'Failed')], null=True)),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.App')),
            ],
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=255)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='JumpServerAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happened_time', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happened_time', models.DateTimeField(auto_now_add=True)),
                ('operation', models.IntegerField(choices=[(0, b'Publish'), (1, b'Backup'), (2, b'Rollback'), (3, b'Startup'), (4, b'Shutdown'), (5, b'DeleteBackup'), (6, b'UnzipWar'), (7, b'CheckApp')])),
                ('username', models.CharField(max_length=30)),
                ('status', models.IntegerField(blank=True, choices=[(0, b'Successfull'), (1, b'Failed')], null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script_name', models.CharField(max_length=30, unique=True)),
                ('script_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=30, unique=True)),
                ('ipaddr', models.GenericIPAddressField(null=True, unique=True)),
                ('port', models.IntegerField(blank=True, default=b'22310', null=True)),
                ('username', models.CharField(default=b'root', max_length=30, null=True)),
                ('password', models.CharField(max_length=40, null=True)),
                ('new_password', models.CharField(blank=True, max_length=40, null=True)),
                ('app_status', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('rollbackup_status', models.CharField(blank=True, max_length=30, null=True)),
                ('ssh_check', models.IntegerField(blank=True, choices=[(0, b'Successfull'), (1, b'Failed')], default=1, null=True)),
                ('change_password_tag', models.IntegerField(blank=True, choices=[(0, b'Successfull'), (1, b'Failed')], default=1, null=True)),
                ('change_password_time', models.DateTimeField(blank=True, null=True)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.App')),
            ],
        ),
        migrations.CreateModel(
            name='ServerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('servers', models.ManyToManyField(to='cmdb.Server')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(choices=[(0, b'Publish'), (1, b'Backup'), (2, b'Rollback'), (3, b'Startup'), (4, b'Shutdown'), (5, b'DeleteBackup'), (6, b'UnzipWar'), (7, b'CheckApp')], null=True)),
                ('total_count', models.IntegerField(default=0)),
                ('complete_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.TaskLog'),
        ),
        migrations.AddField(
            model_name='osuser',
            name='server_group',
            field=models.ManyToManyField(to='cmdb.ServerGroup'),
        ),
        migrations.AddField(
            model_name='logger',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server'),
        ),
        migrations.AddField(
            model_name='logger',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.TaskLog'),
        ),
        migrations.AddField(
            model_name='app',
            name='start_script_path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_script', to='cmdb.Scripts'),
        ),
        migrations.AddField(
            model_name='app',
            name='stop_script_path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_script', to='cmdb.Scripts'),
        ),
    ]
