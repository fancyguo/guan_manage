# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20170410_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='name',
            field=models.CharField(default=None, max_length=120, null=True),
        ),
    ]
