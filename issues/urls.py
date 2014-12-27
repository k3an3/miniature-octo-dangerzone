from django.conf.urls import patterns, url
from issues import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<issue_id>\d+)/$', views.issueDetail, name='detail'),
    url(r'^(?P<issue_id>\d+)/vote/$', views.vote, name='vote'),
    )
