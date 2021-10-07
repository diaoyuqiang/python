from django.shortcuts import render  # render加载模板
from django.http import HttpResponse
from myapp.models import Users
# Create your views here.


def index(res):
    # 执行models操作

    # # 添加操作
    # ob = Users()  # 实例化一个新对象(空对象)
    # ob.name = "王五"
    # ob.age = 19
    # ob.phone = '18573336'
    # ob.save()  # 新对象添加数据
    #
    # # 删除操作
    # mod = Users.objects  # 获取Users的model对象
    # user = mod.get(id=6)  # 获取id为6的数据
    # user.delete()  # 删除数据

    # 修改操作
    # ob = Users.objects.get(id=5)
    # # print(ob.name)
    # ob.name = '小刘'
    # ob.age = 46
    # ob.save()

    # 数据查询
    mod = Users.objects  # 获取Users模型的Model操作对象
    # ul = mod.all()  # 获取所有数据
    # ul = mod.filter(name='小刘')  # filter 过滤条件查询
    # ul = mod.filter(age__gte=22)  # age大于等于22岁
    # ul = mod.order_by('age')[:3]  # 排序：默认升序 | [:3] 获取前三条数据

    # for i in ul:
    #     print(i.name, i.age, i.phone)
    return HttpResponse("首页 <br/> <a href='/users'>用户信息管理</a>")  # 首页添加超链接


# 浏览用户信息
def index_users(res):

    try:

        ul = Users.objects.all()
        context = {'users_list': ul}
        return render(res, 'myapp/users/index.html', context)  # 加载模板

    except:
        return HttpResponse('没有用户信息')


# 加载添加用户信息表单
def add_users(res):
    return render(res, 'myapp/users/add.html')


# 执行用户信息添加
def insert_users(res):

    try:
        ob = Users()  # 实例化一个新对象(空对象)
        # 从表单中获取要添加的信息并封装到ob对象中
        ob.name = res.POST['name']
        ob.age = res.POST['age']
        ob.phone = res.POST['phone']
        ob.save()  # 执行保存
        context = {'info': '添加成功！'}

    except:
        context = {'info': '添加失败！'}

    return render(res, 'myapp/users/info.html', context)


# 执行用户信息删除
def del_users(res, uid=0):

    try:
        ob = Users.objects.get(id=uid)  # 获取要删除的数据
        ob.delete()  # 执行删除操作
        context = {'info': '删除成功！'}

    except:
        context = {'info': '删除失败！'}

    return render(res, 'myapp/users/info.html', context)


# 加载用户信息修改表单
def edit_users(res, uid=0):

    try:
        ob = Users.objects.get(id=uid)  # 获取要修改的数据

        context = {'user': ob}
        return render(res, 'myapp/users/edit.html', context)

    except:
        context = {'info': '没有找到要修改的数据'}

    return render(res, 'myapp/users/info.html', context)


# 执行用户信息修改
def update_users(res):
    try:
        uid = res.POST['id']  # 获取要修改数据的id号
        ob = Users.objects.get(id=uid)  # 查询要修改的数据
        # 从表单中获取要添加的信息并封装到ob对象中
        ob.name = res.POST['name']
        ob.age = res.POST['age']
        ob.phone = res.POST['phone']
        ob.save()  # 执行保存
        context = {'info': '修改成功！'}

    except:
        context = {'info': '修改失败！'}

    return render(res, 'myapp/users/info.html', context)