"""guan_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin, auth
from task.views import TaskListView
from django.contrib.auth import views as auth_views
from .views import user_login, user_logout, user_register
# urlpatterns = [
#     url('^auth/', include('django.contrib.auth.urls')),
# ]
#
# urlpatterns += [
#     # url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', auth_views.login),
#     url(r'^register/$', user_register),
#     url(r'^accounts/$', include(admin.site.urls)),
#     url(r'^task/', TaskListView.as_view()),
# ]

urlpatters = [
    url(r'^login/$', user_login),
    url(r'^logout/$', user_logout),
    url(r'^tasks/$', TaskListView.as_view()),
]