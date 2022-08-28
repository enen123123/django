#coding=utf-8

from django.contrib import admin
from django.urls import path

from stu import views

urlpatterns = [
    path('', views.Index.as_view()),

    path('ren/', views.ren),
    path('ren2/', views.ren2),
    path('ren3/', views.ren3),

    path('tem/', views.tem),

]