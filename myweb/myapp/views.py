from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu
# Create your views here.


def index(request):
    return HttpResponse("hello world!")


def add(request):
    col = Stu.objects.all()  # 获取student表的所有数据
    for item in col:
        print(item)

    print(Stu.objects.get(s_id='01'))  # 查询s_id='01'的数据
    return HttpResponse("add ...")