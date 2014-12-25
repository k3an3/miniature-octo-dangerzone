# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuecomment',
            old_name='item',
            new_name='issue',
        ),
    ]
