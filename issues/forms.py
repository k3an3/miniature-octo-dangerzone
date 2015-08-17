from django import forms
from datetime import timedelta
import issues.models as models

class IssueForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(label="Description:<br>", widget=forms.widgets.Textarea())
    typeof = forms.ChoiceField(choices=models.TYPE_CHOICES, label="Issue Type")
    severity = forms.ChoiceField(choices=models.SEVERITY_CHOICES, label="Issue Severity")
    song = forms.ChoiceField(choices=((song.id, song) for song in models.Song.objects.all()), label="Song")

    class Meta:
        model = models.Issue
        fields = ('title', 'description', 'typeof', 'severity', 'minutes', 'seconds')
        widgets = {
                'minutes': forms.widgets.NumberInput(attrs={'placeholder': 0, 'maxlength': 2, 'style': 'width:40px'}),
                'seconds': forms.widgets.NumberInput(attrs={'placeholder': 0, 'maxlength': 2, 'style': 'width:40px'}),
                }
