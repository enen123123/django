from django.db import models

# Create your models here.


# Admin后台站点
class Clazz(models.Model):
    con=models.AutoField(primary_key=True)
    # 更改cname界面名
    cname=models.CharField(max_length=30,unique=True,verbose_name=u'班级')

    def __unicode__(self):
        return self.cname

    class Meta:
        db_table='t_cls'
#更改admin中表名
        verbose_name_plural=u'班级'

class Student(models.Model):
    son=models.AutoField(primary_key=True,verbose_name=u'学号')
    sname=models.CharField(max_length=30,unique=True,verbose_name=u'学生')
    cls=models.ForeignKey(Clazz,verbose_name=u'班级',on_delete=models.CASCADE)
    # 用来中途添加外键
    # migrations\1(默认值)\''(空)\migrate

    def __unicode__(self):
        return self.sname

    class Meta:
        db_table='t_student'
        verbose_name_plural = u'学生'


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