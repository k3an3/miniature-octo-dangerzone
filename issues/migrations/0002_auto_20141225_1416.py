# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
