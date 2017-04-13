# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime


def ajax_view(func):
    @login_required(login_url='index.html')
    def _render(req, *args, **kwargs):
        if hasattr(req, "method") and req.method == 'OPTIONS':
            return HttpResponse(dict(data=None), status=200, content_type='application/json')

        result = func(req, *args, **kwargs)
        return result
        if isinstance(result, HttpResponse):
            return result

        if isinstance(result, dict):
            data = result
            data.update({'code': 0})
        elif isinstance(result, [list, set, tuple, bool]):
            data = {
                'data': result,
                'code': 0
            }
        return HttpResponse(data, status=200, content_type='application/json')
    return _render


def utc_now():
    return datetime.datetime.now()
