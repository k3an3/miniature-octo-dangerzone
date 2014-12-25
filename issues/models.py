from django.db import models

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

class Issue(models.Model):
    issue_title = models.CharField(max_length=50)
    issue_description = models.CharField(max_length=1000)
    issue_date = models.DateTimeField('date')
    issue_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Suggestion')
    issue_severity = models.CharField(max_length = 100, choices=SEVERITY_CHOICES, default='Trivial')
    issue_status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default='New')
    issue_votes = models.IntegerField(default=0)

class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.CharField(max_length=1000)
    task_date = models.DateTimeField('date')
    task_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Misc')
    task_votes = models.IntegerField(default=0)

class IssueComment(models.Model):
    item = models.ForeignKey(Issue)
    comment_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
