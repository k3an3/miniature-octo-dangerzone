# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_auto_20141227_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcomment',
            old_name='issue',
            new_name='task',
        ),
    ]
