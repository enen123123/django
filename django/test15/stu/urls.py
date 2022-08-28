#coding=utf-8

from django.contrib import admin
from django.urls import path

from stu import views

urlpatterns = [
    path('', views.set_cookie),
    path('get/', views.get_cookie),

]

