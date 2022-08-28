#coding=utf-8

from django.contrib import admin
from django.urls import path,include

from movie import views

urlpatterns = [
    path('',views.index_view),


]