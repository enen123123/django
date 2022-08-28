#coding=utf-8

from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    path('request/', views.request_view),
    path('response/', views.response_view),

]
