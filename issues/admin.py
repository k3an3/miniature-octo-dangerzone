from django.contrib import admin
from issues.models import *

class CommentInIssue(admin.TabularInline):
    model = IssueComment

class CommentInTask(admin.TabularInline):
    model = TaskComment

class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_title', 'issue_description', 'issue_date', 'is_new')
    inlines = [CommentInIssue]

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_description', 'task_date')
    inlines = [CommentInTask]

admin.site.register(Issue, IssueAdmin)
admin.site.register(Task)
admin.site.register(IssueComment)
admin.site.register(TaskComment)
