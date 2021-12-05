from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    # path('add/', views.add, name='add'),  # 路径为add，指定views下的add函数
]