# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0009_song_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(default=b'New', max_length=50, choices=[(b'New', b'New'), (b'Acknowledged', b'Acknowledged'), (b'Fix Proposed', b'Fix Proposed'), (b'Fixed', b'Fixed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'Pro', max_length=50, choices=[(b'New', b'New'), (b'Acknowledged', b'Acknowledged'), (b'Fix Proposed', b'Fix Proposed'), (b'Fixed', b'Fixed')]),
            preserve_default=True,
        ),
    ]
