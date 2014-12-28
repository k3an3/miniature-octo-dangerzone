from django.db import models
from django.utils import timezone

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
    ('Ack', 'Acknowledged'),
    ('Pro', 'Fix Proposed'),
    ('Fix', 'Fixed'),
    )

class Song(models.Model):
    def __str__(self):
        return self.song_title
    title = models.CharField(max_length=50, default='')
    notes = models.CharField(max_length=200, default='None')

class Issue(models.Model):
    def __str__(self):
        return self.title
    def is_new(self):
        return self.status == 'New'
    is_new.boolean = True
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField('date')
    typeof = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Suggestion')
    severity = models.CharField(max_length = 100, choices=SEVERITY_CHOICES, default='Trivial')
    status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default='New')
    votes = models.IntegerField(default=0)
    song = models.ForeignKey(Song)

class Task(models.Model):
    def __str__(self):
        return self.title;
    def is_new(self):
        return self.date >= timezone.now() - datetime.timedelta(days=3)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField('date')
    typeof = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Misc')
    status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default='Pro')
    votes = models.IntegerField(default=0)
    priority = models.CharField(max_length = 100, choices=SEVERITY_CHOICES, default='Trivial')

class IssueComment(models.Model):
    def __str__(self):
        return self.text
    issue = models.ForeignKey(Issue)
    text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

class TaskComment(models.Model):
    def __str__(self):
        return self.text
    task = models.ForeignKey(Task)
    text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

