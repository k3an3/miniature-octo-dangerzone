from django.shortcuts import render, get_object_or_404
from issues.models import Issue
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    issue_recent_list = Issue.objects.order_by('-issue_date')[:25]
    context = {'issue_recent_list' : issue_recent_list}
    return render(request, 'issues/index.html', context)

def issueDetail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    return render(request, 'issues/detail.html', {'issue' : issue})

def vote(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.POST.get('voteup', False):
        issue.issue_votes += 1
    elif request.POST.get('votedown', False):
        issue.issue_votes -= 1
    issue.save()
    return HttpResponseRedirect(reverse('issues:detail', args=(issue.id,)))
