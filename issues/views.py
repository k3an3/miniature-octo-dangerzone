import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from issues.models import *
from issues.forms import *
from issues.utils import *

class IndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issue_recent_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page'] = 'issues'
        return context

    def get_queryset(self):
        return Issue.objects.order_by('-date')

class SongIndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'song_recent_list'

    def get_context_data(self, **kwargs):
        context = super(SongIndexView, self).get_context_data(**kwargs)
        context['page'] = 'songs'
        return context

    def get_queryset(self):
        return Song.objects.order_by('-title')[:25]

class DetailView(generic.DetailView):
    model = Issue
    template_name = 'issues/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['page'] = 'issues'
        context['upvoters'] = Vote.objects.filter(issue=context['issue'], mode='up')
        context['downvoters'] = Vote.objects.filter(issue=context['issue'], mode='down')
        context['comments'] = IssueComment.objects.filter(issue=context['issue']).order_by('-date')
        return context

class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'issues/detail.html'

class IssueCreate(generic.CreateView):
    model = Issue
    template_name = 'issues/new.html'

    def get(self, request, *args, **kwargs):
        form = IssueForm(request.user)
        return self.render_to_response({'form': form, 'page': 'issues',})

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.user, request.POST)
        if form.is_valid():
            form.instance.song = Song.objects.get(id=request.POST.get('song'))
            form.instance.reporter = request.user
            form.save()
            for user in get_editors():
                new_issue_email(user.user.first_name, request.POST.get('title'), user.user.email, reverse('issues:detail', args=(form.instance.id)))
            return redirect('/')
        return self.render_to_response({'form': form, 'page': 'issues',})

class SongCreate(generic.CreateView):
    model = Song
    fields = ['title', 'notes', 'url']
    template_name = 'issues/new.html'

def delete(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    issue.delete()
    return redirect('/')

def delete_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.delete()
    return redirect('/songs/')

def comment(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    text = request.POST.get('text')
    IssueComment.objects.create(user=request.user, text=text, issue=issue)
    for sub in Subscription.objects.filter(issue=issue):
        issue_comment_email(sub.user.first_name, issue.title, sub.user.email, reverse('issues:detail', args=(issue.id,)), text)
    return redirect('/' + issue_id)

def delete_comment(request, issue_id, comment_id):
    comment = get_object_or_404(IssueComment, pk=comment_id)
    comment.delete()
    return redirect('/' + issue_id)

def vote(request, comment_id):
    if request.user.is_authenticated():
        issue = get_object_or_404(Issue, pk=issue_id)
        vote = Vote.objects.filter(user=request.user, issue=issue)
        if not vote:
            if request.POST.get('voteup', False):
                Vote.objects.create(user=request.user, issue=issue, mode='up')
                issue.upvotes += 1
            elif request.POST.get('votedown', False):
                Vote.objects.create(user=request.user, issue=issue, mode='down')
                issue.downvotes += 1
        else:
            vote = vote[0]
            if vote.mode == 'up':
                if request.POST.get('votedown', False):
                    issue.downvotes += 1
                    issue.upvotes -= 1
                    vote.mode = 'down'
            elif vote.mode == 'down':
                if request.POST.get('voteup', False):
                    issue.downvotes -= 1
                    issue.upvotes += 1
                    vote.mode = 'up'
            vote.save()
        issue.save()
        return HttpResponseRedirect(reverse('issues:detail', args=(issue.id,)))
    else:
        return HttpResponse("You can't vote in this poll.")
