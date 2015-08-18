# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0015_auto_20150818_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 12, 53, 7, 147664)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
