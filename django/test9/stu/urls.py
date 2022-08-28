#encoding=utf-8
from django.urls import path

from stu import views

urlpatterns = [
    path('', views.register),
    path('addstu/', views.addstu),
    path('showall/', views.showall),
    path('detail/', views.detail),

]
