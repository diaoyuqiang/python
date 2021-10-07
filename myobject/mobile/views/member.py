from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import Orders, OrderDetail, Member, Shop

# Create your views here.


def index(res):
    # 个人中心首页
    return render(res, 'mobile/member.html')


def orders(res):
    # 浏览订单信息
    mod = Orders.objects
    mid = res.session['mobileuser']['id']  # 会员id号
    olist = mod.filter(member_id=mid)

    # 获取、判断并封装状态status搜索条件
    status = res.GET.get('status', '')
    if status != '':
        olist = olist.filter(status=status)

    list2 = olist.order_by("-id")  # id降序

    # 遍历当前订单，封装订单详情信息
    orders_status = ['无', '排队中', '已撤销', '已完成']
    for vo in list2:
        plist = OrderDetail.objects.filter(order_id=vo.id)[:4]  # 获取头四条
        vo.plist = plist
        vo.statusinfo = orders_status[vo.status]  # 订单状态:1进行中/2无效/3已完成

    # 封装信息加载模板输出
    context = {"orderslist": list2}
    return render(res, "mobile/member_orders.html", context)


def detail(res):
    # 个人中心订单详情
    pid = res.GET.get('pid', 0)
    # 获取当前订单
    order = Orders.objects.get(id=pid)
    # 获取订单详情
    plist = OrderDetail.objects.filter(order_id=order.id)
    order.plist = plist
    # 获取店铺名称信息
    shop = Shop.objects.only('name').get(id=order.shop_id)
    order.shopname = shop.name
    orders_status = ['无', '排队中', '已撤销', '已完成']
    order.statusinfo = orders_status[order.status]
    return render(res, 'mobile/member_detail.html', {'order': order})


def logout(res):
    # 执行会员退出
    del res.session['mobileuser']
    return render(res, 'mobile/register.html')


