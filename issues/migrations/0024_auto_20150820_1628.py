# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0023_auto_20150820_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 16, 28, 58, 590002)),
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 16, 28, 58, 590945)),
        ),
        migrations.AddField(
            model_name='subscription',
            name='issue',
            field=models.ForeignKey(to='issues.Issue'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
