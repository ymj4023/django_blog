#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者       : MJ40
#创建时间   : 2018/12/20 16:25
#文件      : forms.py
#IDE      : PyCharm
#comments/forms.py
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']