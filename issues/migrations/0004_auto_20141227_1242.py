# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_auto_20141227_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='type',
            new_name='typeof',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='type',
            new_name='typeof',
        ),
    ]
