# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0017_auto_20150818_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 13, 3, 36, 270067)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to='issues.SiteUser'),
        ),
    ]
