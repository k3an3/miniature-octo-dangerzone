from django.contrib import admin
from issues.models import *

class CommentInIssue(admin.TabularInline):
    model = IssueComment
    extra = 0

class CommentInTask(admin.TabularInline):
    model = TaskComment
    extra = 0

class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_title', 'issue_description', 'issue_date', 'is_new')
    inlines = [CommentInIssue]
    list_filter = ['issue_date', 'issue_type', 'issue_severity', 'song']
    search_fields = ['issue_title', 'issue_description']
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_description', 'task_date')
    inlines = [CommentInTask]

class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'song_notes')

admin.site.register(Issue, IssueAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(IssueComment)
admin.site.register(TaskComment)
admin.site.register(Song, SongAdmin)
