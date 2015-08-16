from django import forms
from datetime import timedelta
from issues.models import *

class IssueForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    date = forms.DateTimeField('date')
    typeof = forms.CharField(max_length=100)
    severity = forms.CharField(max_length = 100)
    minutes = forms.IntegerField()
    seconds = forms.IntegerField()
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    minutes = forms.IntegerField()
    seconds = forms.IntegerField()
