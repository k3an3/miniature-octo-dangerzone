from django.conf.urls import patterns, url
from issues import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tasks/$', views.TaskIndexView.as_view(), name='task_index'),
    url(r'^songs/$', views.SongIndexView.as_view(), name='song_index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='song_detail'),
    url(r'^(?P<issue_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^tasks/(?P<issue_id>\d+)/vote/$', views.vote, name='task_vote'),
    )
