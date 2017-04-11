# coding=utf-8
from django.db import models
from guan_manage.models import Base
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q, F


class TaskInfo(Base):
    name = models.CharField(default=None, max_length=120, null=True)
    email = models.EmailField(default=None, null=True)
    is_new = models.BooleanField(default=True)  # 标注是否为新增任务信息
    user = models.OneToOneField(User, null=True)
    status = models.CharField(max_length=120, default=None, null=True)
    phone = models.CharField(max_length=120, default=None, null=True)
    remark = models.TextField(default=None, null=True)

    class Meta:
        db_table = 'task_info'


admin.site.register(TaskInfo)
