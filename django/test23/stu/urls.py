from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    path('', views.Areaview.as_view()),
    path('getinfo/', views.getinfo),


]