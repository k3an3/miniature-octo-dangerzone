# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0022_auto_20150820_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='email_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 15, 45, 15, 551527)),
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 15, 45, 15, 552378)),
        ),
    ]
