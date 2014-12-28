from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from issues.models import Issue, Task, Song

class IndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issue_recent_list'

    def get_queryset(self):
        return Issue.objects.order_by('-date')[:25]

class TaskIndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'task_recent_list'

    def get_queryset(self):
        return Task.objects.order_by('-date')[:25]

class SongIndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'song_recent_list'

    def get_queryset(self):
        return Song.objects.order_by('-title')[:25]

class DetailView(generic.DetailView):
    model = Issue
    template_name = 'issues/detail.html'

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'issues/task_detail.html'

class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'issues/song_detail.html'

def vote(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.POST.get('voteup', False):
        issue.votes += 1
    elif request.POST.get('votedown', False):
        issue.votes -= 1
    issue.save()
    return HttpResponseRedirect(reverse('issues:detail', args=(issue.id,)))
