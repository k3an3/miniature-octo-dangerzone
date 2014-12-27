from django.shortcuts import render, get_object_or_404
from issues.models import Issue
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

class IndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issue_recent_list'

    def get_queryset(self):
        return Issue.objects.order_by('-issue_date')[:25]

class DetailView(generic.DetailView):
    model = Issue
    template_name = 'issues/detail.html'

def vote(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.POST.get('voteup', False):
        issue.issue_votes += 1
    elif request.POST.get('votedown', False):
        issue.issue_votes -= 1
    issue.save()
    return HttpResponseRedirect(reverse('issues:detail', args=(issue.id,)))
