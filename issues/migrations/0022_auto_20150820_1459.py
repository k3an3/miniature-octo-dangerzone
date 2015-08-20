# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0021_auto_20150820_1451'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 14, 59, 30, 676867)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 14, 59, 30, 676021)),
        ),
    ]
