from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from issues import views

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'issues/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'issues/logout.html'}, name='logout'),
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^songs/$', login_required(views.SongIndexView.as_view()), name='song_index'),
    url(r'^new/$', login_required(views.IssueCreate.as_view()), name='new_issue'),
    url(r'^delete/(?P<issue_id>\d+)/$', login_required(views.delete), name='delete'),
    url(r'^songs/delete/(?P<song_id>\d+)/$', login_required(views.delete_song), name='delete_song'),
    url(r'^songs/new/$', login_required(views.SongCreate.as_view(success_url="../")), name='new_song'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^songs/(?P<pk>\d+)/$', login_required(views.SongDetailView.as_view()), name='song_detail'),
    url(r'^(?P<issue_id>\d+)/vote/$', login_required(views.vote), name='vote'),
    )
