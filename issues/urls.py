from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from issues import views

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'issues/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'issues/logout.html'}, name='logout'),
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^tasks/$', login_required(views.TaskIndexView.as_view()), name='task_index'),
    url(r'^songs/$', login_required(views.SongIndexView.as_view()), name='song_index'),
    url(r'^new/$', login_required(views.IssueCreate.as_view(success_url="../")), name='new_issue'),
    url(r'^tasks/new/$', login_required(views.TaskCreate.as_view(success_url="../")), name='new_task'),
    url(r'^songs/new/$', login_required(views.SongCreate.as_view(success_url="../")), name='new_song'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^tasks/(?P<pk>\d+)/$', login_required(views.TaskDetailView.as_view()), name='task_detail'),
    url(r'^songs/(?P<pk>\d+)/$', login_required(views.SongDetailView.as_view()), name='song_detail'),
    url(r'^(?P<issue_id>\d+)/vote/$', login_required(views.vote), name='vote'),
    url(r'^tasks/(?P<issue_id>\d+)/vote/$', login_required(views.vote), name='task_vote'),
    )
