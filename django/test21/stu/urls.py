from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [

    path('form/', views.Loginview.as_view()),

    path('form2/', views.Registerview.as_view()),


]
