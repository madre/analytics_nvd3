# coding=utf-8
from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^demo/', include('demo.urls')),
    url(r'^analytics/', include('user_analytics.urls')),
    url(r'^accounts/', include('account.urls')),
    url(r'^backend/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()