from django.contrib import admin

# Register your models here.

# admin站点下加载table
from stu.models import Clazz,Student

# admin表的界面显示方式   写清楚调用的属性名
class Studentadmin(admin.ModelAdmin):
    # 列表展示
    list_display = ['son','sname']
    # 列表过滤
    list_filter = ['son']
    # 搜索框
    search_fields = ['son','sname']
    # 外键关联表的信息
    # raw_id_fields = ['cls']
    # date_hierarchy = ''     用来添加日期字段，必须要自带日期的属性
    # 排序(升序、降序（加负号-）)
    ordering = ['-son']

admin.site.register(Clazz)
admin.site.register(Student,Studentadmin)






# 另一种代替在Terminal中的方法
# Tools\run manage.py Task
# startapp stu
# makemigrations stu
# migrate

# createsuperuser
# Username (leave blank to use '86187'):  admin
# Email address:  hello@163.com
# Warning: Password input may be echoed.
# Password:  12345678
# Warning: Password input may be echoed.
# Password (again):  12345678
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: This password is entirely numeric.
#  y
# Superuser created successfully.

# settings中更改
# 中文站点admin语言
# LANGUAGE_CODE = 'zh-Hans'
# TIME_ZONE = 'Asia/Shanghai'
# USE_TZ = False
