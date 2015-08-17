from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.base import View
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

class SongIndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'song_recent_list'

    def get_queryset(self):
        return Song.objects.order_by('-title')[:25]

class DetailView(generic.DetailView):
    model = Issue
    template_name = 'issues/detail.html'

class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'issues/detail.html'

class IssueCreate(generic.CreateView):
    model = Issue
    template_name = 'issues/new.html'

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.instance.song = Song.objects.get(id=request.POST.get('song'))
            form.instance.reporter = request.user
            form.save()
            return redirect('/')

class SongCreate(generic.CreateView):
    model = Song
    fields = ['title', 'notes', 'url']
    template_name = 'issues/new.html'

def delete(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    issue.delete()
    return redirect('/')

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
