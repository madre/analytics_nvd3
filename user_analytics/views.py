# -*- coding: utf-8  -*-
# !/usr/local/bin/python

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2010, levp-inc, All rights reserved."
__author__ = "madeling <madeling@letvpicture.com>"

from django.views.generic import TemplateView
from utils.redis_cache import REDIS_INS


class UserBasicTemplate(TemplateView):
    template_name = "device.html"

    def get_context_data(self, **kwargs):
        context = super(UserBasicTemplate, self).get_context_data(**kwargs)
        device_wifi_total = REDIS_INS.hget("analytics_wifi_user_", "device_wifi_total")
        context['device_wifi_total'] = device_wifi_total
        user_wifi_total = REDIS_INS.hget("analytics_wifi_user_", "user_wifi_total")
        context['user_wifi_total'] = user_wifi_total
        user_wifi_origin_total = REDIS_INS.hget("analytics_wifi_user_", "user_wifi_origin_total")
        context['user_wifi_origin_total'] = user_wifi_origin_total

        # 报表数据
        xdata = ["设备", "用户", "独立用户"]
        ydata = [device_wifi_total, user_wifi_total, user_wifi_origin_total]

        extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
        chartdata = {
            'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
        }
        charttype = "discreteBarChart"
        chartcontainer = 'discretebarchart_container'  # container name
        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': True,
            },
        }
        context.update(data)
        return context
