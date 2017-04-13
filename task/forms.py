# coding=utf-8
from django.forms import ModelForm
from .models import TaskInfo


class TaskInfoForm(ModelForm):
    class Meta:
        model = TaskInfo
        exclude = ('email', )

