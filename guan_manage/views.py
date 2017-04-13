# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User, Group


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return {'success': True, 'msg': 'login success'}
    else:
        return {'success': False, 'msg': 'login error'}


def user_logout(request):
    logout(request)
    return {'success': True, 'msg': 'logout success'}


def user_register(request, *args, **kwargs):
    register_form = UserCreationForm(request.POST)
    username = request.POST.get('username')
    is_exist_username = User.objects.filter(name=username).exists()
    # 用户名重名
    if is_exist_username:
        register_form.error_messages['username_unique_error'] = 'username is same with other user'
    if not register_form.is_valid() or is_exist_username:
        return HttpResponse({
            'message': register_form.error_messages
        }, status=200, content_type='application/json')

    register_form.save(commit=True)
    login(request, register_form)
    return register_form



