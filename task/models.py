# coding=utf-8
from django.db import models
from guan_manage.models import Base
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db.models import Q, F


@python_2_unicode_compatible
class TaskInfo(Base):
    name = models.CharField(max_length=120, default=None, null=True, blank=True)
    email = models.EmailField(default=None, null=True, blank=True)
    is_new = models.BooleanField(default=True)  # 标注是否为新增任务信息
    user_id = models.CharField(max_length=120, default=None, null=True, blank=True)
    status = models.CharField(max_length=120, default=None, null=True, blank=True)
    phone = models.CharField(max_length=120, default=None, null=True, blank=True)
    remark = models.TextField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'task_info'


admin.site.register(TaskInfo)
