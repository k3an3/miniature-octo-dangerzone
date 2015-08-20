from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

TYPE_CHOICES = (
    ('Suggestion', 'Suggestion'),
    ('Editing Issue', 'Editing Issue'),
    ('Mix Issue', 'Mix Issue'),
    ('Timing Issue', 'Timing Issue'),
    ('Pitch Issue', 'Pitch Issue'),
    ('Misc.', 'Misc.'),
)
SEVERITY_CHOICES = (
    ('Trivial', 'Trivial'),
    ('Minor', 'Minor'),
    ('Major', 'Major'),
    ('Severe', 'Severe'),
)
STATUS_CHOICES = (
    ('New', 'New'),
    ('Acknowledged', 'Acknowledged'),
    ('Fix Proposed', 'Fix Proposed'),
    ('Resolved', 'Resolved'),
    )
VOTE_CHOICES = (
    ('up', 'up'),
    ('down', 'down'),
    )
ROLE_CHOICES = (
    ('reporter', 'Reporter'),
    ('editor', 'Editor'),
    )


class SiteUser(models.Model):
    def __str__(self):
        return self.user.username

    user = models.ForeignKey(User)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email_notifications = models.BooleanField(default=True)

class Song(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=50, default='')
    notes = models.CharField(max_length=200, default='None')
    url = models.CharField(max_length=500, default='')


class Issue(models.Model):
    def __str__(self):
        return self.title

    def is_new(self):
        return self.status == 'New'

    def timecode(self):
        minutes = self.seconds / 60
        seconds = self.seconds % 60
        return "%d:%02d" % (minutes, seconds)

    is_new.boolean = True
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.datetime.now())
    typeof = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Suggestion')
    severity = models.CharField(max_length = 100, choices=SEVERITY_CHOICES, default='Trivial')
    status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default='New')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    song = models.ForeignKey(Song)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    reporter = models.CharField(max_length=30)


class IssueComment(models.Model):
    def __str__(self):
        return self.text

    issue = models.ForeignKey(Issue)
    text = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    user = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now())


class Vote(models.Model):
    def __str__(self):
        return self.user.username + " | " + self.issue.title

    issue = models.ForeignKey(Issue)
    user = models.ForeignKey(User)
    mode = models.CharField(max_length=10, choices=VOTE_CHOICES)

class Subscription(models.Model):
    issue = models.ForeignKey(Issue)
    user = models.ForeignKey(User)
