# 员工信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import User
from django.core.paginator import Paginator
from django.db.models import Q  # 封装或条件
from datetime import datetime
import hashlib
import random


def index(res, pIndex=1):
    # 浏览信息
    umod = User.objects
    ulist = umod.filter(status__lt=9)  # 过滤数据，已删除的不展示

    # mywhere: 封装过滤条件
    mywhere = []
    # 获取并判断搜索条件
    kw = res.GET.get("keyword", None)
    if kw:
        # Q: 多条件搜索
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))  # __contains: 模糊查询
        mywhere.append('keyword=' + kw)

    # 获取、判断并封装状态status搜索条件
    status = res.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append('status=' + status)

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

    context = {"userlist": list2, 'plist': plist, 'pIndex': pIndex, 'pages': pages, 'mywhere': mywhere}
    return render(res, "myadmin/user/index.html", context)


def add(res):
    # 加载信息添加表单
    return render(res, 'myadmin/user/add.html')


def insert(res):
    # 执行信息添加
    try:
        ob = User()
        ob.username = res.POST['username']
        ob.nickname = res.POST['nickname']
        # 获取密码并md5
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = res.POST['password'] + str(n)  # 从表单获取密码并添加干扰值
        md5.update(s.encode('utf-8'))  # 更新md5子串
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n  # 加盐

        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功！'}

    except Exception as err:
        context = {'info': '添加失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def delete(res, uid=0):
    # 执行信息删除
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功！'}

    except Exception as err:
        context = {'info': '删除失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def edit(res, uid=0):
    # 加载信息编辑表单
    try:
        ob = User.objects.get(id=uid)
        context = {'user': ob}
        return render(res, 'myadmin/user/edit.html', context)

    except Exception as err:
        context = {'info': '没有找到要修改的信息'}
        print(err)
        return render(res, 'myadmin/info.html', context)


def update(res, uid=0):
    # 执行信息编辑
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = res.POST['nickname']
        ob.status = res.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '修改成功！'}

    except Exception as err:
        context = {'info': '修改失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)