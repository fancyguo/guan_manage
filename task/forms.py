# coding=utf-8
from django.forms import ModelForm
from .models import TaskInfo, TaskRelate


class TaskInfoForm(ModelForm):
    class Meta:
        model = TaskInfo
        exclude = ('email', )


class TaskRelateForm(ModelForm):
    class Meta:
        model = TaskRelate
        exclude = ('task_infos', 'user')
