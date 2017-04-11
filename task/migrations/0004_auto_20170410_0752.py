# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20170410_0751'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='taskrelate',
            table='task_relate',
        ),
    ]
