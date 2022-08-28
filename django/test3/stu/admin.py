from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Student)
# http://127.0.0.1:8000/admin/  通过这个可以直接访问


'''
    python manage.py  可以直接查看所有的命令
    python manage.py createsuperuser  创建超级用户
    Username (leave blank to use '86187'): admin
    Email address: hello@163.com
    Password:123
    Password (again):123
    This password is too short. It must contain at least 8 characters.
    This password is too common.
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    
    数据库auth_user中存储着账户信息
    用来登录Django administration
    站点访问信息
    LANGUAGE_CODE = 'zh-Hans'
    # en-us英文   zh-Hans中文
    TIME_ZONE = 'Asia/Shanghai'
    # 更改以上两个后会中文化
'''