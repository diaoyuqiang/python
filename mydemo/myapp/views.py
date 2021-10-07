from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse  # 根据路由名称反向生成url请求地址
from django.shortcuts import redirect  # 重定向
# Create your views here.


def index(res):
    print(reverse('find'))  # url反向解析
    print(reverse('index'))
    print(reverse('find3', args=(10, "dyq")))
    # return HttpResponse("HELLO WORLD!")
    return redirect(reverse('find3', args=(10, "dyq")))  # 执行页面请求重定向


def add(res, sid):
    return HttpResponse("add! %d" % sid)


def find(res, sid=1, name=''):
    return HttpResponse("find %d:%s" % (sid, name))


def fun(res, year, month):
    return HttpResponse("年月：%s-%s" % (year, month))


def update(res):
    # return HttpResponse("update...!")
    raise Http404('请求页面不存在！')  # 自定义404错误信息
