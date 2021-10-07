# 订单信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator  # 分页类
from datetime import datetime
from myadmin.models import Orders, OrderDetail, Payment, User, Member


def index(res, pIndex=1):
    # 浏览订单信息
    omod = Orders.objects
    shop_id = res.session['shopinfo']['id']  # 店铺id号
    mywhere = []
    list = omod.filter(shop_id=shop_id)

    # 获取、判断并封装状态status搜索条件
    status = res.GET.get('status', '')
    if status != '':
        list = list.filter(status=status)
        mywhere.append("status=" + status)

    list = list.order_by('-id')  # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 10)  # 以10条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    for vo in list2:
        if vo.user_id == 0:
            vo.nickname = "无"
        else:
            user = User.objects.only('nickname').get(id=vo.user_id)  # only:仅查询nickname
            vo.nickname = user.nickname

        if vo.member_id == 0:
            vo.membername = "大堂顾客"
        else:
            member = Member.objects.only('mobile').get(id=vo.member_id)
            vo.membername = member.mobile

    # 封装信息加载模板输出
    context = {"orderslist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere,
               'url': res.build_absolute_uri()}
    return render(res, "web/list.html", context)


def insert(res):
    # 执行订单添加
    # 大堂执行订单添加操
    try:
        # 执行订单信息添加操作
        od = Orders()
        od.shop_id = res.session['shopinfo']['id']  # 店铺id号
        od.member_id = 0  # 会员id设置为0
        od.user_id = res.session['webuser']['id']  # 操作员id
        od.money = res.session['total_money']
        od.status = 1  # 订单状态:1进行中/2无效/3已完成
        od.payment_status = 2  # 支付状态:1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        # 执行支付信息添加
        op = Payment()
        op.order_id = od.id  # 订单id号
        op.member_id = 0  # 会员id号
        op.money = res.session['total_money']  # 支付款
        op.type = 2  # 付款方式：1会员付款/2收银收款
        op.bank = res.GET.get("bank", 3)  # 收款银行渠道:1微信/2余额/3现金/4支付宝
        op.status = 2  # 支付状态:1未支付/2已支付/3已退款
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        # 执行订单详情添加
        cartlist = res.session.get('cartlist', {})  # 获取购物车中的菜品信息
        # 遍历购物车商品添加到订单详情表中
        for shop in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id
            ov.product_id = shop['id']
            ov.product_name = shop['name']
            ov.price = shop['price']
            ov.quantity = shop['num']
            ov.status = 1
            ov.save()

        # 清空购物车
        # 清空总金额
        del res.session['cartlist']
        del res.session['total_money']
        return HttpResponse("y")

    except Exception as err:
        print(err)
        return HttpResponse("n")


def detail(res):
    # 浏览订单信息
    oid = res.GET.get("oid", 0)
    dlist = OrderDetail.objects.filter(order_id=oid)
    context = {"detaillist": dlist}

    return render(res, 'web/detail.html', context)


def status(res):
    # 修改订单状态
    try:
        oid = res.GET.get("oid", '0')  # 获取oid
        ob = Orders.objects.get(id=oid)
        ob.status = res.GET['status']
        ob.save()
        return HttpResponse("y")
    except Exception as err:
        print(err)
        return HttpResponse("n")


