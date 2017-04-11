# coding=utf-8
import tempfile
from django.views.generic import ListView, DetailView
from utils import tools, error_code
from .db import *
from .forms import TaskInfoForm
from pyExcelerator.ImportXLS import parse_xls
from pyExcelerator import Workbook
from django.db import transaction
from django.http import HttpResponse



class TaskListView(ListView):
    @tools.ajax_view
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user or user.is_authenticated():
            return {
                'code': error_code.USER_NO_LOGIN
            }
        req_type = request.GET.get('type', None)
        if user.is_superuser():
            return TaskInfo.objects.filter(deleted=False)
        if req_type == 'distributed':
            return get_task_by_user_id(user['id'])
        return undistributed_task()

    @tools.ajax_view
    def delete(self, request, *args, ** kwargs):
        ids = request.GET.getlist('ids')
        remove_task(ids)
        return True

    @tools.ajax_view
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        ids = request.POST.get('ids')

        # 取消任务
        if action == 'cancel':
            cancel_task(ids)
            return get_task_by_ids(ids)
        # 重新分配任务
        elif action == 'redistribute':
            user_id = request.POST.get('user_id')
            if not user_id:
                return False
            redistribute_task(ids, user_id)
            return get_task_by_ids(ids)
        # 导入
        elif action == 'import':
            def handle(key):
                return sheets[key] if sheets.has_key(key) else None
            user_file = request.FILES.values()[0]
            _, xls = tempfile.mkstemp()
            with open(xls, 'wb') as f:
                f.write(user_file.read())
            sheets = parse_xls(xls)[0][1]

            with transaction.atomic():
                tasks = []
                for i in range(1, max(sheets.keys())[0]+1):
                    task = TaskInfo()
                    task.name = handle((i, 0))
                    task.email = handle((i, 1))
                    task.remark = handle((i, 2))
                    task.is_new = True
                    tasks.append(task)
                TaskInfo.objects.bulk_create(tasks)
            return undistributed_task()
        # 导出
        elif action == 'export':
            tasks = TaskInfo.objects.filter(deleted=0)
            w = Workbook()
            ws = w.add_sheet()
            for r, task in enumerate(tasks):
                r += 1
                ws.write(r, 0, task.name)
                ws.write(r, 1, task.email)
                ws.write(r, 2, task.phone)
                ws.write(r, 3, task.remark)
            _, xls = tempfile.mkstemp()
            w.save(xls)

            response = HttpResponse(open(xls).read(),
                                    content_type='application/xls')
            response['Content-Disposition'] = 'attachment; filename=users.xls'
            return response

