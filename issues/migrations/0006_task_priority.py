# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20141227_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'Trivial', max_length=100, choices=[(b'Trivial', b'Trivial'), (b'Minor', b'Minor'), (b'Major', b'Major'), (b'Severe', b'Severe')]),
            preserve_default=True,
        ),
    ]
