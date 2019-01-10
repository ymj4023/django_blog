#!/usr/bin/env python
# _*_coding:utf-8_*_
# 作者       : MJ40
# 创建时间   : 2019/1/10 17:11
# 文件      : search_indexs.py
# IDE      : PyCharm
#blog/search_indexes.py

from haystack import indexes
from.models import Post

class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Post


    def index_queryset(self, using=None):
        return self.get_model().objects.all()
