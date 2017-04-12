# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User, Group


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return "login success"
    else:
        return "invalid login"


def logout_view(request):
    logout(request)


def user_register(request, *args, **kwargs):
    register_form = UserCreationForm(request.POST)
    is_exist_username = User.objects.filter(name=register_form.username).exists()
    # 用户名重名
    if is_exist_username:
        register_form.error_messages['username_unique_error'] = 'username is same with other user'
    if not register_form.is_valid() or is_exist_username:
        return HttpResponse({
            'message': register_form.error_messages
        }, status=200, content_type='application/json')

    register_form.save(commit=True)
    login(request, register_form)



