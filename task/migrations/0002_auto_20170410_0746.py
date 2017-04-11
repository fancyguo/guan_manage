# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='taskinfo',
            name='remark',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='taskrelate',
            name='remark',
            field=models.TextField(default=None, null=True),
        ),
    ]
