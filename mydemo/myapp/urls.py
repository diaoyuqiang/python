from django.urls import path, re_path
from . import views

# myapp应用的路由配置
urlpatterns = [
    path('', views.index, name='index'),  # 寻址views.index函数
    path('add/<int:sid>', views.add, name='add'),  # 路径转换器: 参数变量地址<类型：参数名>
    path('find/', views.find, name='find'),
    path('find/<int:sid>', views.find),
    path('find/<int:sid>/<str:name>', views.find, name='find3'),
    re_path(r'^fun/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.fun),  # 正则路径（?P<year>[0-9]{4}）
    path('edit/', views.update),
]