# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_issue_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='url',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
