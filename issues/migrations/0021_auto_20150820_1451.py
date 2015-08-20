# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0020_auto_20150820_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcomment',
            name='task',
        ),
        migrations.RemoveField(
            model_name='issuecomment',
            name='postedby',
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='user',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 14, 50, 43, 300475)),
        ),
        migrations.DeleteModel(
            name='TaskComment',
        ),
    ]
