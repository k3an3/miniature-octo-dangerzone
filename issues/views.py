from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from issues.models import Issue, Task, Song
from issues.forms import IssueForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate

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
    template_name = 'issues/detail.html'

class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'issues/detail.html'

class IssueCreate(generic.CreateView):
    model = Issue
    fields = ['title', 'typeof', 'severity', 'song', 'seconds', 'description']
    template_name = 'issues/new.html'

    def form_valid(self, form):
        form.instance.date = datetime.datetime.now()
        form.instance.postedby = self.user
        return super(IssueCreate, self).form_valid(form)

class TaskCreate(generic.CreateView):
    model = Task
    fields = ['title', 'typeof', 'priority', 'description']
    template_name = 'issues/new.html'

    @permission_required('user.can_create')
    def form_valid(self, form):
        form.instance.date = datetime.datetime.now()
        return super(TaskCreate, self).form_valid(form)

class SongCreate(generic.CreateView):
    model = Song
    fields = ['title', 'notes', 'url']
    template_name = 'issues/new.html'

def vote(request, issue_id):
    if request.user.is_authenticated() and request.user.has_perm('issues.can_vote'):
        issue = get_object_or_404(Issue, pk=issue_id)
        if request.POST.get('voteup', False):
            issue.upvotes += 1
        elif request.POST.get('votedown', False):
            issue.downvotes += 1
        issue.save()
        return HttpResponseRedirect(reverse('issues:detail', args=(issue.id,)))
    else:
        return HttpResponse("You can't vote in this poll.")
