# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0012_auto_20150114_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('role', models.CharField(max_length=20, choices=[('reporter', 'Reporter'), ('editor', 'Editor')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('mode', models.CharField(max_length=10, choices=[('up', 'up'), ('down', 'down')])),
            ],
        ),
        migrations.RemoveField(
            model_name='issue',
            name='postedby',
        ),
        migrations.AddField(
            model_name='issue',
            name='reporter',
            field=models.CharField(default='nobody', max_length=30),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='severity',
            field=models.CharField(default='Trivial', max_length=100, choices=[('Trivial', 'Trivial'), ('Minor', 'Minor'), ('Major', 'Major'), ('Severe', 'Severe')]),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(default='New', max_length=50, choices=[('New', 'New'), ('Acknowledged', 'Acknowledged'), ('Fix Proposed', 'Fix Proposed'), ('Fixed', 'Fixed')]),
        ),
        migrations.AlterField(
            model_name='issue',
            name='typeof',
            field=models.CharField(default='Suggestion', max_length=100, choices=[('Suggestion', 'Suggestion'), ('Editing Issue', 'Editing Issue'), ('Mix Issue', 'Mix Issue'), ('Timing Issue', 'Timing Issue'), ('Pitch Issue', 'Pitch Issue'), ('Misc.', 'Misc.')]),
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='postedby',
            field=models.CharField(default='nobody', max_length=30),
        ),
        migrations.AlterField(
            model_name='song',
            name='notes',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='postedby',
            field=models.CharField(default='nobody', max_length=30),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default='Trivial', max_length=100, choices=[('Trivial', 'Trivial'), ('Minor', 'Minor'), ('Major', 'Major'), ('Severe', 'Severe')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='Pro', max_length=50, choices=[('New', 'New'), ('Acknowledged', 'Acknowledged'), ('Fix Proposed', 'Fix Proposed'), ('Fixed', 'Fixed')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='typeof',
            field=models.CharField(default='Misc', max_length=50, choices=[('Suggestion', 'Suggestion'), ('Editing Issue', 'Editing Issue'), ('Mix Issue', 'Mix Issue'), ('Timing Issue', 'Timing Issue'), ('Pitch Issue', 'Pitch Issue'), ('Misc.', 'Misc.')]),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='postedby',
            field=models.CharField(default='nobody', max_length=30),
        ),
        migrations.AddField(
            model_name='vote',
            name='issue',
            field=models.ForeignKey(to='issues.Issue'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to='issues.SiteUser'),
        ),
    ]
