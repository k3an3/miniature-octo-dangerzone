from django import forms
from datetime import timedelta

class IssueForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    minutes = forms.IntegerField()
    seconds = forms.IntegerField()