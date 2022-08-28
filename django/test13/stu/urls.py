#coding=utf-8

#from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from stu import views
from test13.settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    path('upload/',views.upload),
    path('toupload/', views.toupload),
    path('showall/', views.showall),
    path('watch/', views.watch),
    path('down/', views.down),

    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

]
if DEBUG:
    urlpatterns += re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

