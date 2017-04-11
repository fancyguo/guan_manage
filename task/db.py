# coding=utf-8
from django.contrib.auth.models import User
from .models import TaskInfo


def get_task_by_ids(ids):
    if not ids:
        return []
    if not isinstance(ids, list):
        ids = [int(ids)]
    return TaskInfo.objects.filter(id__in=ids)


def get_task_by_user_id(user_id):
    return TaskInfo.objects.filter(deleted=False, user__id=user_id)


def undistributed_task():
    return TaskInfo.objects.filter(user__isnull=True, deleted=False)


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
    user = User.objects.get(pk=user_id)
    if not user:
        return []
    for task in tasks:
        task.user.update(user)
