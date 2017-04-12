# coding=utf-8
from django.contrib.auth.models import User
from .models import TaskInfo


# 获取指定的任务
def get_task_by_ids(ids):
    if not ids:
        return []
    if not isinstance(ids, list):
        ids = [int(ids)]
    return TaskInfo.objects.filter(id__in=ids)


# 获取某人的任务
def get_task_by_user_id(user_id):
    return TaskInfo.objects.filter(deleted=False, user_id=user_id)


# 未分配任务
def undistributed_task():
    return TaskInfo.objects.filter(user_id__isnull=True, deleted=False)


# 删除任务
def remove_task(ids):
    tasks = get_task_by_ids(ids)
    for task in tasks:
        task.remove()


# 取消分配的任务
def cancel_task(ids):
    tasks = get_task_by_ids(ids)
    for task in tasks:
        task.user.remove()


# 重新分配
def redistribute_task(ids, user_id):
    tasks = get_task_by_ids(ids)
    for task in tasks:
        task.update({'user_id': user_id})
