#blog/views.py


import markdown
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post,Category
# Create your views here.


def index(request):
    """这里我们使用 all() 方法从数据库里获取了全部的文章，存在了 post_list 变量里。
    all 方法返回的是一个 QuerySet（可以理解成一个类似于列表的数据结构），由于通常来说博客文章列表是按文章发表时间倒序排列的，
    即最新的文章排在最前面，所以我们紧接着调用了 order_by 方法对这个返回的 queryset 进行排序。
    排序依据的字段是 created_time，即文章的创建时间。- 号表示逆序，如果不加 - 则是正序。 接着如之前所做，
    我们渲染了 blog\index.html 模板文件，并且把包含文章列表数据的 post_list 变量传给了模板。"""
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


def detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    #阅读量+1
    post.increase_views()

    #记得在顶部引入markdown 模块
    #给markdown渲染函数传递了额外的参数extensions,增加扩展
    post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',#语法高亮扩展
        'markdown.extensions.toc',#允许自动生成目录
    ])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request,year,month):

    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request,'blog/index.html', context={'post_list': post_list})


def category(request,pk):

    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html', context={'post_list': post_list})