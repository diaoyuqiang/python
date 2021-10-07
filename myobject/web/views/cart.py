# 购物车信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# 引入随机函数模块
import random
from PIL import Image, ImageDraw, ImageFont


def add(res, pid):
    # 添加购物车
    # 从session中获取所有菜品信息，从中获取要放入购物车中的菜品
    product = res.session['productlist'][pid]
    product['num'] = 1  # 初始化当前菜品的购买量
    # 尝试从session中获取购物车信息,没有返回空{}
    cartlist = res.session.get('cartlist', {})
    # 判断当前购物车中是否已存在选中的菜品
    if pid in cartlist:
        cartlist[pid]['num'] += product['num']  # 增加购物量

    else:
        cartlist[pid] = product  # 放进购物车

    # 将cartlist放进session
    res.session['cartlist'] = cartlist
    print(cartlist)
    # 跳转到点餐首页
    return redirect(reverse('web_index'))


def delete(res, pid):
    # 删除购物车商品
    cartlist = res.session.get('cartlist', {})
    del cartlist[pid]  # 删除指定菜品id的商品
    # 将cartlist放进session
    res.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))


def clear(res):
    # 清空购物车
    res.session['cartlist'] = {}
    return redirect(reverse('web_index'))


def change(res):
    # 更改购物车信息操作

    # 尝试从session中获取购物车信息,没有返回空{}
    cartlist = res.session.get('cartlist', {})
    pid = res.GET.get('pid', 0)  # 获取要修改的菜品id
    m = int(res.GET.get('num', 1))  # 菜品要修改的数量
    if m < 1:
        m = 1

    cartlist[pid]['num'] = m  # 修改购物车中的数量

    # 将cartlist放进session
    res.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))