# -*- coding: utf-8  -*-
# !/usr/bin/env python
"""

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2010, levp-inc, All rights reserved."
__author__  = "madeling <madeling@letvpicture.com>"
"""
from django.conf.urls import patterns, url
from account.views import LoginView, LogOutView

urlpatterns = patterns('',
                       url(r'^login/$', LoginView.as_view(), name='login'),
                       url(r'^logout/$', LogOutView.as_view(), name='logout'),
                       )