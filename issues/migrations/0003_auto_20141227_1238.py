# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20141225_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='issue_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_severity',
            new_name='severity',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_votes',
            new_name='votes',
        ),
        migrations.RenameField(
            model_name='issuecomment',
            old_name='comment_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_notes',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_votes',
            new_name='votes',
        ),
        migrations.RenameField(
            model_name='taskcomment',
            old_name='comment_text',
            new_name='text',
        ),
    ]
