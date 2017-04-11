# coding=utf-8
from django.contrib.auth import authenticate, login, logout


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


