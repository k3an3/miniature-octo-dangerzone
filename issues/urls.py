from django.conf.urls import patterns, url
from issues import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<issue_id>\d+)/vote/$', views.vote, name='vote'),
    )
