# -*- coding: utf-8  -*-
# !/usr/bin/env python
"""

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2010, levp-inc, All rights reserved."
__author__  = "madeling <madeling@letvpicture.com>"
"""

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from user_analytics.views import UserBasicTemplate

urlpatterns = patterns('',
                       url(r'^$', login_required(UserBasicTemplate.as_view()), name='home'),
                       )