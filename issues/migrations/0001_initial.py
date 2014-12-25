# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_title', models.CharField(max_length=50)),
                ('issue_description', models.CharField(max_length=1000)),
                ('issue_date', models.DateTimeField(verbose_name=b'date')),
                ('issue_type', models.CharField(default=b'Suggestion', max_length=100, choices=[(b'Suggestion', b'Suggestion'), (b'Editing Issue', b'Editing Issue'), (b'Mix Issue', b'Mix Issue'), (b'Timing Issue', b'Timing Issue'), (b'Pitch Issue', b'Pitch Issue'), (b'Misc.', b'Misc.')])),
                ('issue_severity', models.CharField(default=b'Trivial', max_length=100, choices=[(b'Trivial', b'Trivial'), (b'Minor', b'Minor'), (b'Major', b'Major'), (b'Severe', b'Severe')])),
                ('issue_status', models.CharField(default=b'New', max_length=50, choices=[(b'New', b'New'), (b'Ack', b'Acknowledged'), (b'Pro', b'Fix Proposed'), (b'Fix', b'Fixed')])),
                ('issue_votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=1000)),
                ('votes', models.IntegerField(default=0)),
                ('item', models.ForeignKey(to='issues.Issue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_title', models.CharField(max_length=50)),
                ('task_description', models.CharField(max_length=1000)),
                ('task_date', models.DateTimeField(verbose_name=b'date')),
                ('task_type', models.CharField(default=b'Misc', max_length=50, choices=[(b'Suggestion', b'Suggestion'), (b'Editing Issue', b'Editing Issue'), (b'Mix Issue', b'Mix Issue'), (b'Timing Issue', b'Timing Issue'), (b'Pitch Issue', b'Pitch Issue'), (b'Misc.', b'Misc.')])),
                ('task_votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
