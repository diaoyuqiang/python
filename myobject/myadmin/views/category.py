# 菜品类别管理视图文件
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from myadmin.models import Category, Shop
from django.core.paginator import Paginator
from datetime import datetime
import hashlib
import random


def index(res, pIndex=1):
    # 浏览信息
    umod = Category.objects
    clist = umod.filter(status__lt=9)  # 过滤数据，已删除的不展示

    # mywhere: 封装过滤条件
    mywhere = []
    # 获取并判断搜索条件
    kw = res.GET.get("keyword", None)
    if kw:

        clist = clist.filter(username__contains=kw)  # __contains: 模糊查询
        mywhere.append('keyword=' + kw)

    # 获取、判断并封装状态status搜索条件
    status = res.GET.get('status', '')
    if status != '':
        clist = clist.filter(status=status)
        mywhere.append('status=' + status)

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(clist, 10)  # 10条一页
    pages = page.num_pages  # 获取总页数

    # 判断当前页是否越界
    if pIndex >= pages:
        pIndex = pages
    if pIndex <= 1:
        pIndex = 1

    list2 = page.page(pIndex)  # 获取当前页数据
    # 获取页码列表信息
    plist = page.page_range  # 获取页码列表

    # 遍历当前菜品分类信息对象并封装店铺信息
    for vo in list2:
        sob = Shop.objects.get(id=vo.shop_id)
        vo.shopname = sob.name

    context = {"categorylist": list2, 'plist': plist, 'pIndex': pIndex, 'pages': pages, 'mywhere': mywhere}
    return render(res, "myadmin/category/index.html", context)


def loadCategory(request,sid):
    clist = Category.objects.filter(status__lt=9, shop_id=sid).values("id", "name")
    # 返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data': list(clist)})


def add(res):
    # 加载信息添加表单
    # 获取当前店铺信息
    slist = Shop.objects.values('id', 'name')
    context = {'shoplist': slist}
    return render(res, 'myadmin/category/add.html', context)


def insert(res):
    # 执行信息添加
    try:
        ob = Category()
        ob.shop_id = res.POST['shop_id']
        ob.name = res.POST['name']

        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功！'}

    except Exception as err:
        context = {'info': '添加失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def delete(res, cid=0):
    # 执行信息删除
    try:
        ob = Category.objects.get(id=cid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功！'}

    except Exception as err:
        context = {'info': '删除失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def edit(res, cid=0):
    # 加载信息编辑表单
    try:
        ob = Category.objects.get(id=cid)
        context = {'category': ob}
        # 获取当前店铺信息
        slist = Shop.objects.values('id', 'name')
        context['shoplist'] = slist
        return render(res, 'myadmin/category/edit.html', context)

    except Exception as err:
        context = {'info': '没有找到要修改的信息'}
        print(err)
        return render(res, 'myadmin/info.html', context)


def update(res, cid=0):
    # 执行信息编辑
    try:
        ob = Category.objects.get(id=cid)
        ob.shop_id = res.POST['shop_id']
        ob.name = res.POST['name']
        ob.status = res.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '修改成功！'}

    except Exception as err:
        context = {'info': '修改失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)