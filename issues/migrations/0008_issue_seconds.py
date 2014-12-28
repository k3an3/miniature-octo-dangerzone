# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='seconds',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
