#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '2015/4/13'
__author__ = 'deling.ma'
"""
import redis
from django.conf import settings


REDIS_INS = redis.Redis(host=settings.REDIS_HOST,
                        port=settings.REDIS_PORT,
                        db=settings.REDIS_DB)