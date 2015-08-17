# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0013_auto_20150815_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Acknowledged', 'Acknowledged'), ('Fix Proposed', 'Fix Proposed'), ('Resolved', 'Resolved')], default='New', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Acknowledged', 'Acknowledged'), ('Fix Proposed', 'Fix Proposed'), ('Resolved', 'Resolved')], default='Pro', max_length=50),
        ),
    ]
