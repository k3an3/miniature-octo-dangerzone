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
    song_title = models.CharField(max_length=50, default='')
    song_notes = models.CharField(max_length=200, default='None')

class Issue(models.Model):
    def __str__(self):
        return self.issue_title
    def is_new(self):
        return self.issue_status == 'New'
    is_new.boolean = True
    issue_title = models.CharField(max_length=50)
    issue_description = models.CharField(max_length=1000)
    issue_date = models.DateTimeField('date')
    issue_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Suggestion')
    issue_severity = models.CharField(max_length = 100, choices=SEVERITY_CHOICES, default='Trivial')
    issue_status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default='New')
    issue_votes = models.IntegerField(default=0)
    song = models.ForeignKey(Song)

class Task(models.Model):
    def __str__(self):
        return task_title;
    def is_new(self):
        return self.task_date >= timezone.now() - datetime.timedelta(days=3)
    task_title = models.CharField(max_length=50)
    task_description = models.CharField(max_length=1000)
    task_date = models.DateTimeField('date')
    task_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Misc')
    task_votes = models.IntegerField(default=0)

class IssueComment(models.Model):
    def __str__(self):
        return comment_text
    issue = models.ForeignKey(Issue)
    comment_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

class TaskComment(models.Model):
    def __str__(self):
        return comment_text
    issue = models.ForeignKey(Task)
    comment_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

