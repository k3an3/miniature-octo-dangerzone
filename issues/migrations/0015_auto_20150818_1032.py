# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0014_auto_20150817_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 10, 32, 17, 995991)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='reporter',
            field=models.CharField(max_length=30),
        ),
    ]
