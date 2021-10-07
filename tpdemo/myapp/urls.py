from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('demo1', views.demo1, name='demo1'),
    path('demo2', views.demo2, name='demo2'),
    # 城市级联操作
    path('showdistrict/', views.showdistrict, name='showdistrict'),  # 加载网页
    path('district/<int:upid>', views.district, name='district'),  # Ajax加载城市信息
]