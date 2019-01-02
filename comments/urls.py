#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者       : MJ40
#创建时间   : 2018/12/20 16:26
#文件      : urls.py
#IDE      : PyCharm
#comments/urls.py

from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]