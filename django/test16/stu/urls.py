from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    path('login/', views.login),
    path('tologin/', views.tologin),


]