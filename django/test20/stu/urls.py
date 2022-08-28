from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    path('', views.index_view),
    path('mw/', views.index_view1),

#CSRF
    path('index2/', views.index_view2),
]