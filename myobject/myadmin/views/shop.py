# 店铺信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import Shop
from django.core.paginator import Paginator
from datetime import datetime
import hashlib
import random
import time


def index(res, pIndex=1):
    # 浏览信息
    smod = Shop.objects
    slist = smod.filter(status__lt=9)  # 过滤数据，已删除的不展示

    # mywhere: 封装过滤条件
    mywhere = []
    # 获取并判断搜索条件
    kw = res.GET.get("keyword", None)
    if kw:
        # Q: 多条件搜索
        slist = slist.filter(name__contains=kw)  # __contains: 模糊查询
        mywhere.append('keyword=' + kw)

    # 获取、判断并封装状态status搜索条件
    status = res.GET.get('status', '')
    if status != '':
        slist = slist.filter(status=status)
        mywhere.append('status=' + status)

    slist = slist.order_by("id")  # 对id进行排序

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 5)  # 5条一页
    pages = page.num_pages  # 获取总页数

    # 判断当前页是否越界
    if pIndex > pages:
        pIndex = pages
    if pIndex < 1:
        pIndex = 1

    list2 = page.page(pIndex)  # 获取当前页数据
    # 获取页码列表信息
    plist = page.page_range  # 获取页码列表

    context = {"shoplist": list2, 'plist': plist, 'pIndex': pIndex, 'pages': pages, 'mywhere': mywhere}
    return render(res, "myadmin/shop/index.html", context)


def add(res):
    # 加载信息添加表单
    return render(res, 'myadmin/shop/add.html')


def insert(res):
    # 执行信息添加
    try:
        # 店铺封面图片的上传处理
        myfile = res.FILES.get("cover_pic", None)
        if not myfile:
            return HttpResponse("没有店铺封面上传文件信息")
        cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/shop/" + cover_pic, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 店铺logo图片的上传处理
        myfile = res.FILES.get("banner_pic", None)
        if not myfile:
            return HttpResponse("没有店铺logo上传文件信息")
        banner_pic = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/shop/" + banner_pic, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 实例化model对象，封装信息，并执行添加
        ob = Shop()
        ob.name = res.POST['name']
        ob.address = res.POST['address']
        ob.phone = res.POST['phone']
        ob.cover_pic = cover_pic
        ob.banner_pic = banner_pic
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功！'}

    except Exception as err:
        context = {'info': '添加失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def delete(res, sid=0):
    # 执行信息删除
    try:
        ob = Shop.objects.get(id=sid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功！'}

    except Exception as err:
        context = {'info': '删除失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def edit(res, sid=0):
    # 加载信息编辑表单
    try:
        ob = Shop.objects.get(id=sid)
        context = {'shop': ob}
        return render(res, 'myadmin/shop/edit.html', context)

    except Exception as err:
        context = {'info': '没有找到要修改的信息'}
        print(err)
        return render(res, 'myadmin/info.html', context)


def update(res, sid=0):
    # 执行信息编辑
    try:
        ob = Shop.objects.get(id=sid)
        ob.name = res.POST['name']
        ob.address = res.POST['address']
        ob.phone = res.POST['phone']
        ob.status = res.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '修改成功！'}

    except Exception as err:
        context = {'info': '修改失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)