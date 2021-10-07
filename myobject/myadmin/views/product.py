# 菜品信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import Category, Shop, Product
from django.core.paginator import Paginator
from datetime import datetime
import hashlib
import random
import time, os


def index(res, pIndex=1):
    # 浏览信息
    umod = Product.objects
    clist = umod.filter(status__lt=9)  # 过滤数据，已删除的不展示

    # mywhere: 封装过滤条件
    mywhere = []
    # 获取并判断搜索条件
    kw = res.GET.get("keyword", None)
    if kw:
        clist = clist.filter(name__contains=kw)  # __contains: 模糊查询
        mywhere.append('keyword=' + kw)

        # 获取并判断搜索菜品类别条件
    cid = res.GET.get("category_id", None)
    if cid:
        clist = clist.filter(category_id=cid)  # __contains: 模糊查询
        mywhere.append('category_id='+cid)

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

    # 遍历当前菜品信息对象并封装店铺和菜品类别信息
    for vo in list2:
        sob = Shop.objects.get(id=vo.shop_id)
        vo.shopname = sob.name
        cob = Category.objects.get(id=vo.category_id)  # 获取对应id的菜品分类对象
        vo.categoryname = cob.name  # 将菜品分类对象的name字段封装到给品信息的categoryname

    context = {"productlist": list2, 'plist': plist, 'pIndex': pIndex, 'pages': pages, 'mywhere': mywhere}
    return render(res, "myadmin/product/index.html", context)


def add(res):
    # 加载信息添加表单
    # 获取当前店铺信息
    slist = Shop.objects.values('id', 'name')
    context = {'shoplist': slist}
    return render(res, 'myadmin/product/add.html', context)


def insert(res):
    # 执行信息添加
    try:
        # 图片的上传处理
        myfile = res.FILES.get("cover_pic", None)
        if not myfile:
            return HttpResponse("没有封面上传文件信息")
        cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/product/" + cover_pic, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        ob = Product()
        ob.shop_id = res.POST['shop_id']
        ob.category_id = res.POST['category_id']
        ob.name = res.POST['name']
        ob.price = res.POST['price']
        ob.cover_pic = cover_pic
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功！'}

    except Exception as err:
        context = {'info': '添加失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def delete(res, pid=0):
    # 执行信息删除
    try:
        ob = Product.objects.get(id=pid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功！'}

    except Exception as err:
        context = {'info': '删除失败！'}
        print(err)

    return render(res, 'myadmin/info.html', context)


def edit(res, pid=0):
    # 加载信息编辑表单
    try:
        ob = Product.objects.get(id=pid)
        context = {'product': ob}
        # 获取当前店铺信息
        slist = Shop.objects.values('id', 'name')
        context['shoplist'] = slist
        return render(res, 'myadmin/product/edit.html', context)

    except Exception as err:
        context = {'info': '没有找到要修改的信息'}
        print(err)
        return render(res, 'myadmin/info.html', context)


def update(res, pid=0):
    # 执行信息编辑
    try:
        # 获取原图片
        oldpicname = res.POST['oldpicname']
        # 图片的上传处理
        myfile = res.FILES.get("cover_pic", None)
        if not myfile:
            cover_pic = oldpicname
        else:
            cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
            destination = open("./static/uploads/product/" + cover_pic, "wb+")
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()

        ob = Product.objects.get(id=pid)
        ob.shop_id = res.POST['shop_id']
        ob.category_id = res.POST['category_id']
        ob.name = res.POST['name']
        ob.price = res.POST['price']
        ob.cover_pic = cover_pic
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '修改成功！'}

        # 判断并删除老图片
        if myfile:
            os.remove('./static/uploads/product/'+oldpicname)

    except Exception as err:

        context = {'info': '修改失败！'}
        print(err)

        # 判断并删除新图片
        if myfile:
            os.remove('./static/uploads/product/' + cover_pic)

    return render(res, 'myadmin/info.html', context)