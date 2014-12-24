from django.db import models

class Issue(models.Model):
    TYPE_CHOICES = (
        (SUGGESTION, 'Suggestion'),
        (EDIT_DEFECT, 'Editing Issue'),
        (MIX_ISSUE, 'Mix Issue'),
        (TIMING_ISSUE, 'Timing Issue'),
        (PITCH_ISSUE, 'Pitch Issue'),
        (MISC_ISSUE, 'Misc.'),
    )
    SEVERITY_CHOICES = (
        (TRIVIAL, 'Trivial'),
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (SEVERE, 'Severe'),
    )
    STATUS_CHOICES = (
        (NEW, 'New'),
        (ACK, 'Acknowledged'),
        (PRO, 'Fix Proposed'),
        (FIX, 'Fixed'),
        )
    issue_title = models.CharField(max_length=50)
    issue_description = models.CharField(max_length=1000)
    issue_date = models.DateTimeField('date')
    issue_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=SUGGESTION)
    issue_severity = models.CharField(max_length = 100, choices=SEVERITY_CHOICES, default=TRIVIAL)
    issue_status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default=NEW)
    issue_votes = models.IntegerField(default=0)

class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.CharField(max_length=1000)
    task_date = models.DateTimeField('date')
    task_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=MISC_ISSUE)
    task_votes = modesl.IntegerField(default=0)

class IssueComment(models.Model):
    item = models.ForeignKey(Issue)
    comment_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
