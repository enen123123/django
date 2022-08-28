from django.db import models

# Create your models here.

class Clazz(models.Model):
    cno=models.AutoField(primary_key=True,)
    cname=models.CharField(max_length=30,unique=True)

    class Meta:
        db_table='t_cls'

    def __unicode__(self):
        return u'Clazz:%s'%self.cname

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    cls=models.ForeignKey(Clazz,on_delete=models.CASCADE)   #一对多，外键
    # on_delete=models.CASCADE  附表需要级联，models要写，myaql要改
    class Meta:
        db_table='t_stu2'

    def __unicode__(self):
        return u'Student:%s'%self.sname

# from stu2.models import *     插入模块
# ccls1=Clazz.objects.create(cno=101,cname=u'101班')   创建
# Student.objects.create(sname='张55',cls=cls1)  子创建
# Clazz.objects.first().student_set.all()   获取所有内容，正向
# Student.objects.first().cls   反向获取
# cls1=Clazz.objects.first()    获取第一个
# Student.objects.create(sname='张5',cls=cls1)   以第一个为基础，创建新的
# Clazz.objects.first().student_set.all()   将该内容对应下的全部展示
# 建立一个函数插入多表
# def insertdate(cname,*snames):
#     try:
#         cls=Clazz.objects.get(cname=cname)
#     except Clazz.DoesNotExist:
#         cls = Clazz.objects.create(cname=cname)
#     for sn in snames:
#         try:
#             Student.objects.get(sname=sn)
#         except Student.DoesNotExist:
#             Student.objects.create(sname=sn,cls=cls)
# 调用并插入
# insertdate('107前端','张德')

