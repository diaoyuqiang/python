# 会员信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import Member
from django.core.paginator import Paginator
from datetime import datetime
import hashlib
import random


def index(res, pIndex=1):
    # 浏览信息
    umod = Member.objects
    ulist = umod.filter(status__lt=9)  # 过滤数据，已删除的不展示
    # mywhere: 封装过滤条件
    mywhere = []
    # 判断并处理状态的搜索条件
    status = res.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append('status=' + status)

    ulist = ulist.order_by('id')  # 对id进行排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 5)  # 5条一页
    pages = page.num_pages  # 获取总页数

    # 判断当前页是否越界
    if pIndex > pages:
        pIndex = pages
    if pIndex < 1:
        pIndex = 1

    list2 = page.page(pIndex)  # 获取当前页数据
    # 获取页码列表信息
    plist = page.page_range  # 获取页码列表

    context = {"memberlist": list2, 'plist': plist, 'pIndex': pIndex, 'pages': pages, 'mywhere': mywhere}
    return render(res, "myadmin/member/index.html", context)


def delete(res, uid=0):
    # 执行信息删除
    try:
        ob = Member.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功！'}

    except Exception as err:
        context = {'info': '删除失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)
