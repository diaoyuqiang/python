from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 配置users操作路由
    path('users', views.index_users, name='index_users'),
    path('users/add', views.add_users, name='add_users'),
    path('users/insert', views.insert_users, name='insert_users'),
    path('users/del/<int:uid>', views.del_users, name='del_users'),
    path('users/edit/<int:uid>', views.edit_users, name='edit_users'),
    path('users/update', views.update_users, name='update_users'),

]