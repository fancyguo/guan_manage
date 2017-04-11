# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=None, max_length=120)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('remark', models.TextField(default=None)),
                ('is_new', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'task_info',
            },
        ),
        migrations.CreateModel(
            name='TaskRelate',
            fields=[
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.CharField(default=None, max_length=100, null=True)),
                ('remark', models.TextField(default=None)),
                ('task_infos', models.ManyToManyField(to='task.TaskInfo')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
