# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0010_auto_20141227_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='postedby',
            field=models.CharField(default=b'nobody', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='postedby',
            field=models.CharField(default=b'nobody', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='postedby',
            field=models.CharField(default=b'nobody', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='postedby',
            field=models.CharField(default=b'nobody', max_length=30),
            preserve_default=True,
        ),
    ]
