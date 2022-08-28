from django.contrib import admin
from django.urls import path, include

from stu import views

urlpatterns = [
    path('', views.getAjax),
    path('get/', views.getview),
    path('post/', views.postview),

    path('only/', views.Onlyview.as_view()),
    path('getinfo/', views.getinfo),

]