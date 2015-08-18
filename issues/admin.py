from django.contrib import admin
from issues.models import *

class CommentInIssue(admin.TabularInline):
    model = IssueComment
    extra = 0

class CommentInTask(admin.TabularInline):
    model = TaskComment
    extra = 0

class IssueInSong(admin.TabularInline):
    model = Issue
    extra = 10

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'is_new')
    inlines = [CommentInIssue]
    list_filter = ['date', 'typeof', 'severity', 'song']
    search_fields = ['title', 'description']

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    inlines = [CommentInTask]
    list_filter = ['date', 'typeof']
    search_fields = ['title', 'description']

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'notes')
    inlines = [IssueInSong]

admin.site.register(Issue, IssueAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(IssueComment)
admin.site.register(TaskComment)
admin.site.register(Song, SongAdmin)
admin.site.register(Vote)
admin.site.register(SiteUser)
