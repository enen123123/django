from django.contrib import admin
from django.urls import path, re_path, include
# path：用于普通路径，不需要自己手动添加正则首位限制符号，底层已经添加。
# re_path：用于正则路径，需要自己手动添加正则首位限制符号。
from stu import views

urlpatterns = [
    # 普通
    path('', views.query1_view),
    # 正则表达式设置   需要模块re_path
    # 位置传参
    re_path(r'^query2/(\d+)$', views.query2_view),
    # 固定参数名  关键字
    re_path(r'^query3/(?P<num3>[A-Za-z0-9]+)$', views.query3_view),
    # 传参数（参数名一致）
    path('query4/', views.query4_view,{'hello':'333'}),
    # 逆向    通过其他路由查找其属性，找到另一个路由的地址
    path('query5/', views.query5_view,name='q1'),
    path('query6/', views.query6_view),

]