#coding=utf-8

from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    # 基于函数def的调用
    path('', views.setsession),
    path('get/', views.getsession),
    path('login/', views.login),
    path('main/', views.main),
    # 基于类class的调用
    path('index/', views.Indexview.as_view()),

]