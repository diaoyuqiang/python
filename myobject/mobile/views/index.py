from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from myadmin.models import Member, Shop, Category, Product, Orders, OrderDetail, Payment
from datetime import datetime


def index(res):
    # 移动端首页
    # 获取并判断当前店铺信息
    shopinfo = res.session.get("shopinfo", None)
    if not shopinfo:
        # 重定向到登录页
        return redirect(reverse('mobile_shop'))  # 重定向到店铺首页

    # 获取当前店铺下的菜品类别和菜品信息
    clist = Category.objects.filter(shop_id=shopinfo['id'], status=1)
    productlist = {}
    for vo in clist:
        plist = Product.objects.filter(category_id=vo.id, status=1)
        productlist[vo.id] = plist
    context = {'categorylist': clist, 'productlist': productlist.items(), 'cid': clist[0]}

    return render(res, 'mobile/index.html', context)


def register(res):
    # 移动端会员登录/注册
    return render(res, 'mobile/register.html')


def doRegister(res):
    # 执行移动端会员登录/注册
    # 短信验证
    verifycode = "1234"  # res.session['verifycode']
    if verifycode != res.POST['code']:
        context = {"info": "验证码错误"}
        return render(res, 'mobile/register.html', context)

    try:
        # 根据手机号码获取当前会员信息
        member = Member.objects.get(mobile=res.POST['mobile'])

    except Exception as err:
        # print(err)
        # # 执行当前会员注册
        ob = Member()
        ob.nickname = "顾客"
        ob.avatar = "moren.png"
        ob.mobile = res.POST['mobile']
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        member = ob

    # 检验当前会员状态
    if member.status == 1:
        # 将当前会员信息转换成字典并放入session中
        res.session['mobileuser'] = member.toDict()
        # 重定向到登录页
        return redirect(reverse('mobile_index'))

    else:
        context = {"info": "此账户信息禁用"}
        return render(res, 'mobile/register.html', context)


def shop(res):
    # 移动端选择店铺
    context = {'shoplist': Shop.objects.filter(status=1)}
    return render(res, 'mobile/shop.html', context)


def selectShop(res):
    # 执行移动端店铺选择
    # return render(res, 'mobile/shop.html')
    # 获取选择的店铺信息并放到session中
    sid = res.GET['sid']
    ob = Shop.objects.get(id=sid)
    res.session['shopinfo'] = ob.toDict()
    # 清空购物车
    res.session['cartlist'] = {}
    # 跳转到首页
    return redirect(reverse('mobile_index'))


def addOrders(res):
    # 移动端下单
    # 从session中获取购物车
    cartlist = res.session.get('cartlist', {})
    total_money = 0  # 初始化总金额

    # 遍历购物车中的菜品并累加总金额
    for vo in cartlist.values():
        total_money += vo['num'] * vo['price']

    res.session["total_money"] = total_money  # 把总金额放进session
    return render(res, 'mobile/addOrders.html')


def doAddOrders(res):
    # 执行订单添加
    od = Orders()
    # 大堂执行订单添加操
    try:
        # 执行订单信息添加操作
        od = Orders()
        od.shop_id = res.session['shopinfo']['id']  # 店铺id号
        od.member_id = res.session['mobileuser']['id']
        od.user_id = 0  # 会员id设置为0
        od.money = res.session['total_money']
        od.status = 1  # 订单状态:1进行中/2无效/3已完成
        od.payment_status = 2  # 支付状态:1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        # 执行支付信息添加
        op = Payment()
        op.order_id = od.id  # 订单id号
        op.member_id = res.session['mobileuser']['id']  # 会员id号
        op.type = 2  # 付款方式：1会员付款/2收银收款
        op.bank = res.GET.get("bank", 3)  # 收款银行渠道:1微信/2余额/3现金/4支付宝
        op.money = res.session['total_money']  # 支付款
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

    except Exception as err:
        print(err)
    return render(res, 'mobile/orderinfo.html', {'order': od})

