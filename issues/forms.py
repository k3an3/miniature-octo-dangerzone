from django import forms
from datetime import timedelta
from django.contrib.auth.models import User
import issues.models as models

class IssueForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['song'] = forms.ModelChoiceField(queryset=models.Song.objects.all())

    title = forms.CharField(max_length=100)
    description = forms.CharField(label="Description:<br>", widget=forms.widgets.Textarea())
    typeof = forms.ChoiceField(choices=models.TYPE_CHOICES, label="Issue Type")
    severity = forms.ChoiceField(choices=models.SEVERITY_CHOICES, label="Issue Severity")

    class Meta:
        model = models.Issue
        fields = ('title', 'description', 'typeof', 'severity', 'minutes', 'seconds')
        widgets = {
                'minutes': forms.widgets.NumberInput(attrs={'placeholder': 0, 'maxlength': 2, 'style': 'width:40px'}),
                'seconds': forms.widgets.NumberInput(attrs={'placeholder': 0, 'maxlength': 2, 'style': 'width:40px'}),
                }

class AccountForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
