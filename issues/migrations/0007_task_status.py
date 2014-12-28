# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'Pro', max_length=50, choices=[(b'New', b'New'), (b'Ack', b'Acknowledged'), (b'Pro', b'Fix Proposed'), (b'Fix', b'Fixed')]),
            preserve_default=True,
        ),
    ]
