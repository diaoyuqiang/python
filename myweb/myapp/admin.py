from django.contrib import admin

# Register your models here.

from myapp.models import Stu

# admin.site.register(Stu)


# 装饰器
@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('s_id', 's_name', 's_birth', 's_sex')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('s_id', 's_name')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('s_id',)  # -s_id降序

    # list_editable 设置默认可编辑字段
    # list_editable = ['s_name', 's_birth']
