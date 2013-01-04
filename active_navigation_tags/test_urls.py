from django.conf.urls import patterns, include, url

from .test_views import dummy_view

urlpatterns = patterns('',
    url(r'^$', dummy_view, name='index'),
    url(r'^modules/$', dummy_view, name='modules'),
    url(r'^modules/module$', dummy_view, name='module'),
    url(r'^blog$', dummy_view, name='blog'),
)
