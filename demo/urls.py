#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '2015/4/8'
__author__ = 'deling.ma'
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('demo.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^piechart/', 'demo_piechart', name='demo_piechart'),
    url(r'^linechart/', 'demo_linechart', name='demo_linechart'),
    url(r'^linechart_without_date/', 'demo_linechart_without_date', name='demo_linechart_without_date'),
    url(r'^linewithfocuschart/', 'demo_linewithfocuschart', name='demo_linewithfocuschart'),
    url(r'^multibarchart/', 'demo_multibarchart', name='demo_multibarchart'),
    url(r'^stackedareachart/', 'demo_stackedareachart', name='demo_stackedareachart'),
    url(r'^multibarhorizontalchart/', 'demo_multibarhorizontalchart', name='demo_multibarhorizontalchart'),
    url(r'^lineplusbarchart/', 'demo_lineplusbarchart', name='demo_lineplusbarchart'),
    url(r'^linechart_with_ampm/', 'demo_linechart_with_ampm', name='demo_linechart_with_ampm'),
    url(r'^cumulativelinechart/', 'demo_cumulativelinechart', name='demo_cumulativelinechart'),
    url(r'^discretebarchart/', 'demo_discretebarchart', name='demo_discretebarchart'),
    url(r'^discretebarchart_with_date/', 'demo_discretebarchart_with_date', name='demo_discretebarchart_with_date'),
    url(r'^scatterchart/', 'demo_scatterchart', name='demo_scatterchart'),

)
