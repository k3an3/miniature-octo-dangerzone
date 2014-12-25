# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20141225_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=1000)),
                ('votes', models.IntegerField(default=0)),
                ('issue', models.ForeignKey(to='issues.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
