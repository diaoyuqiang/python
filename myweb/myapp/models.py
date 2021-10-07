from django.db import models

# Create your models here.


# 自定义Stu表继承Model类
# 定义属性：sql列
class Stu(models.Model):

    # 字段类型及长度
    s_id = models.CharField("学号", max_length=20, primary_key=True)
    s_name = models.CharField("名称", max_length=20)
    s_birth = models.CharField("生日", max_length=20)
    s_sex = models.CharField("性别", max_length=10)

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s" % (self.s_id, self.s_name, self.s_birth, self.s_sex)

    # 自定义对应的表名，默认表名：student
    class Meta:
        db_table = "student"
        verbose_name = '浏览学生信息'  # 进入学生信息管理的提示
        verbose_name_plural = '学生信息管理'  # 站点管理首页展示
