from django.shortcuts import render, redirect  # render:渲染导入模板 redirect: 重定向
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.urls import reverse
from django.views import View
# Create your views here.


def index(res):
    return render(res, 'myapp/index.html')


# 简单的视图响应
def resp01(res):
    return HttpResponse('<h3>简单的视图响应</h3>')


# 错误响应
def resp02(res):
    # return HttpResponseNotFound('<h2>Page Not Found</h2>')
    # return HttpResponse(status=403)  # 响应状态码
    raise Http404('does not exist')  # Http404404: 请求页面不存在


# 重定向
def resp03(res):
    # redirect: 重定向  reverse: 反向解析url地址
    # return redirect(reverse('resp01'))
    # js代码重定向
    return HttpResponse('<script> alert("跳转成功"); location.href="/resp01"; </script>')


# 基于类的视图
class MyView(View):

    def get(self, res, *args, **kwargs):
        return HttpResponse('hell view!')


# json数据的响应
def resp05(res):
    data = [
        {'id': 1001, 'name': '张三', 'age': 18},
        {'id': 1002, 'name': '李四', 'age': 20},
        {'id': 1003, 'name': '王五', 'age': 22}
    ]

    return JsonResponse({"data": data})  # 必须以字典的形式


# cookie的使用
# def resp06(res):
#     # 获取当前的 响应对象
#     response = HttpResponse('cookie的设置')
#     # 使用响应对象进行cookie的设置
#     response.set_cookie('a', 'abc')
#     # 获取cookie信息
#     print(res.COOKIES.get('a', None))
#     # 返回响应对象
#     return response


def resp07(res):
    # 读取
    m = res.COOKIES.get('num', None)
    if m:
        m = int(m) + 1
    else:
        m = 1
    # 获取当前的响应对象
    response = HttpResponse('cookie记录的计数器值：' + str(m))
    # 使用响应对象进行cookie的设置
    response.set_cookie('num', m)
    # 返回响应对象
    return response


# 测试res请求对象
def resp08(res):
    print('请求路径:', res.path)
    print('请求方法:', res.method)
    print('请求编码:', res.encoding)
    # 获取页面请求参数
    print('id:', res.GET['id'])
    print('age:', res.GET.get('age', default=None))

    return HttpResponse('测试res请求对象')


# 验证码的输出
def test_code(res):

    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bg_color = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25

    # 创建画面对象
    im = Image.new('RGB', (width, height), bg_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象
    font = ImageFont.truetype('static/ariali.ttf', 23)
    font = ImageFont.load_default().font
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    # res.session['test_code'] = rand_str
    # 内存文件操作
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')