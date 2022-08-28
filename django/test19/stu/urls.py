from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    path('', views.index),
    # 过滤器
    path('f1', views.f1),
    # 自定义过滤器
    path('f2', views.f2),
]
