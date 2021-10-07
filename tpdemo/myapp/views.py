from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from myapp.models import District

# Create your views here.


def index(res):
    return render(res, 'myapp/index.html')


def demo1(res):
    # 模板语法
    context = dict()
    context['name'] = 'zhangsan'
    context['a'] = [10, 20, 30]
    context['stu'] = {'name': 'lisi', 'age': 20}
    data = [
        {'name': '张翠山', 'sex': 1, 'age': 40, 'state': 0},
        {'name': '殷素素', 'sex': 0, 'age': 30, 'state': 2},
        {'name': '张无忌', 'sex': 1, 'age': 20, 'state': 1},
        {'name': '赵敏', 'sex': 0, 'age': 18, 'state': 2},
    ]
    context['dist'] = data
    context['time'] = datetime.now()
    context['m1'] = 100
    context['m2'] = 200
    return render(res, 'myapp/demo1.html', context)


def demo2(res):
    # 模板继承
    return render(res, 'myapp/demo2.html')


# 加载城市级联信息操作模板
def showdistrict(request):
    return render(request, "myapp/district.html")


# 加载对应的城市信息函数，返回json数据格式
def district(res, upid=0):
    dlist = District.objects.filter(upid=upid)  # 获取数据库模型对象
    mylist = []
    for ob in dlist:  # 遍历对象中的数据并以字典的形式添加到列表中
        mylist.append({'id': ob.id, 'name': ob.name})
    return JsonResponse({'data': mylist})
