from django.db import models
from datetime import datetime
# Create your models here.


class Users(models.Model):

    # 字段类型及长度
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    create_time = models.DateTimeField(default=datetime.now())

    # class Meta:
    #     db_table = "myapp_users"  # 指定表名,默认为myapp_users