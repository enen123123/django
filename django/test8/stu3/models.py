from django.db import models

# Create your models here.


class Course(models.Model):
    courseid = models.AutoField(primary_key=True,)
    coursename = models.CharField(max_length=30,unique=True)

    class Meta:
        db_table = 't_course'

    def __unicode__(self):
        return u'Course:%s'%self.coursename

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    course=models.ManyToManyField(Course)     #多对多  会产生三张表

    class Meta:
        db_table='t_stu3'

    def __unicode__(self):
        return u'Student:%s'%self.sname

# from stu3.models import *
# c1=Course.objects.create(courseid='1010',coursename='html')
# c2=Course.objects.create(coursename='cs')
# s1=Student.objects.create(sno=1001,sname='张三')
# s2=Student.objects.create(sname='张四')
# 只能主表add附表
# s2.course.add(c2)
# s1.course.add(c1,c2)
# Course.objects.first().student_set.all()
# Student.objects.first().course.all()
# 函数调用
# def insertdate(sname,*coursenames):
#     try:
#         stu=Student.objects.get(sname=sname)
#     except Student.DoesNotExist:
#         stu = Student.objects.create(sname=sname)
#     cnlist=[]
#     for cn in coursenames:
#         try:
#             course=Course.objects.get(coursename=cn)
#         except Course.DoesNotExist:
#             course = Course.objects.create(coursename=cn)
#         cnlist.append(course)
#     stu.course.add(*cnlist)
# 填入数据，可填入多个课程
# insertdate('王五','js')


# 参数讲解
# *args,**kwargs    元组、字典（可传递，可不传递）
# 建造函数
# def demo(*args,**kwargs):
#     print (args)
#     print (kwargs)
# 调用函数
# demo()
# 结果
# ()
# {}
# 只元组
# demo('a','b')
# ('a', 'b')
# {}
# 只字典
# demo(a=1,b=2)
# ()
# {'a': 1, 'b': 2}
# 形参：a,b,c
# def demo2(a,b,c):
#     print(a,b,c)
# 实参：1,2,3
# demo2(1,2,3)
# 1 2 3
# 压缩包，传入函数，再解包(元组){字典}
# args=('a1','a2','a3')
# demo2(*args)
# a1 a2 a3
# kwargs={'a':'b1','b':'b2','c':'b3'}
# demo2(**kwargs)
# b1 b2 b3