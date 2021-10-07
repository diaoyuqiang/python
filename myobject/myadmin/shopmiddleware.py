# 自定义中间件类
from django.shortcuts import redirect
from django.urls import reverse

import re  # 正则模块


class ShopMiddleware(object):

    def __init__(self, get_response):  # 中间件的init方法在程序启动时调用
        self.get_response = get_response
        # One-time configuration and initialization.
        print("ShopMiddleware")

    def __call__(self, res):
        # 获取当前请求路径
        path = res.path
        print("url:"+path)

        # 判断管理后台是否登录
        # 定义后台直接访问的url列表
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin', '/myadmin/verify']

        # 判断当前请求url地址是否以/myadmin开头,并且不在urllist中，才做登录判断
        if re.match(r'^/myadmin', path) and (path not in urllist):

            # 判断是否登录(key名为adminuser的信息是否存在于session中)
            if 'adminuser' not in res.session:
                # 重定向到登录页
                return redirect(reverse('myadmin_login'))

        # 判断大堂点餐前台是否登录，(session中是否有webuser)
        if re.match(r'^/web', path):
            # 判断是否登录(key名为adminuser的信息是否存在于session中)
            if 'webuser' not in res.session:
                # 重定向到登录页
                return redirect(reverse('web_login'))

        # 判断移动端是否登录
        # 定义移动端直接访问的url列表
        urllist = ['/mobile/register', '/mobile/doregister']

        # 判断当前请求url地址是否以/mobile开头,并且不在urllist中，才做登录判断
        if re.match(r'^/mobile', path) and (path not in urllist):

            # 判断是否登录(key名为mobileuser的信息是否存在于session中)
            if 'mobileuser' not in res.session:
                # 重定向到登录页
                return redirect(reverse('mobile_register'))

        response = self.get_response(res)
        return response