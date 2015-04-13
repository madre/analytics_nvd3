# -*- coding: utf-8  -*-
# !/usr/bin/env python
"""

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2010, levp-inc, All rights reserved."
__author__  = "madeling <madeling@letvpicture.com>"
"""
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.views.generic.base import TemplateResponseMixin


class LoginView(View, TemplateResponseMixin):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect("home")
        next_redirect = request.GET.get("next")
        return self.render_to_response({"next": next_redirect, "message": "欢迎进入数据统计系统"})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return self.render_to_response({"error": "请输入用户名或密码"})
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.POST.get("next"):
                    return redirect(request.POST.get("next"))
                print "no next"
                return redirect("home")
            else:
                # Return a 'disabled account' error message
                return self.render_to_response({"error": "用户未激活，请联系管理员"})
        else:
            # Return an 'invalid login' error message.
            return self.render_to_response({"error": "用户名或密码错误"})


class LogOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")