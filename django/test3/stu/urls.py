# coding=utf-8

from django.urls import path
# from django.template.defaulttags import url

from . import views
urlpatterns=[
    path('',views.index_view),
    path('register/', views.regieter),
    path('show/', views.show),

]
