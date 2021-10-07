from django.urls import path, include
from . import views
from .views import MyView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('resp01', views.resp01, name='resp01'),  # 第一个参数为url路径，name:url的名字，用来做反向解析
    path('resp02', views.resp02, name='resp02'),  # 返回一个错误
    path('resp03', views.resp03, name='resp03'),  # 重定向
    path('resp04', MyView.as_view(), name='resp04'),  # 基于视图类的方法
    path('resp05', views.resp05, name='resp05'),  # 响应json格式
    # path('resp06', views.resp06, name='resp06'),  # cookie的使用
    path('resp07', views.resp07, name='resp07'),  # cookie计数器
    path('resp08', views.resp08, name='resp08'),  # 测试res请求对象
    path('resp09', views.test_code, name='resp09'),  # 验证码的输出
]
