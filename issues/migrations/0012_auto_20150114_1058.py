# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_auto_20141228_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='votes',
            new_name='downvotes',
        ),
        migrations.RenameField(
            model_name='issuecomment',
            old_name='votes',
            new_name='downvotes',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='votes',
            new_name='downvotes',
        ),
        migrations.AddField(
            model_name='issue',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
