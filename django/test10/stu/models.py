from django.db import models

# Create your models here.
# from django.db.models import Manager

# 构造objects隐藏(逻辑删除)函数
# class Custommanger(Manager):
#     def all(self):
#         return Manager.all(self).filter(isdelete=False)

class Student(models.Model):
    sname=models.CharField(max_length=30)
    isdelete=models.BooleanField(default=False)


    # # 通过建造一个新的函数，代替系统自带的，以实现特殊的目的
    # objects=Custommanger()
    # 也可以更改原系统函数更深层次的函数

    # # 构造新的delete函数
    # def delete(self, using=None, keep_parents=False):
    #     self.isdelete=True
    #     self.save()


    class Meta():
        # 表的另一个名字
        db_table='t_student'

    def __unicode__(self):
        return u'Student:%s'%self.sname


# Student.objects.all()
# Student.delete()
# Student.objects.filter()

# 参考现成的基础函数，构建需要的各种函数，可以用class\def

#
class Self(models.Model):
    sname=models.CharField(max_length=30)
    # 数字，总数为3，小数占两位
    score=models.DecimalField(max_digits=3,decimal_places=2)
# 引包
# from stu.models import *
# from django.db.models import *
# 聚合函数  最大、最小、条数、平均、总共
# Self.objects.aggregate(Max('id'))
# Self.objects.aggregate(Min('id'))
# Self.objects.aggregate(Count('id'))
# Self.objects.aggregate(Avg('id'))
# Self.objects.aggregate(Sum('id'))

# 分组聚合  相同类下的对应其他属性（暂时是数字）累计、平均、条数
# Self.objects.values('sname').annotate(Sum('score'))
# Self.objects.values('sname').annotate(Avg('score'))
# Self.objects.values('sname').annotate(Count('score'))

# 子查询   同类下平均值的最大值
# Self.objects.values('sname').annotate(s=Avg('score')).aggregate(Max('s'))

# 关联查询  必须通过外键连接相关的属性，达到在某条件下完成目的
# Self.objects.values('score__sname')

# 原生查询  必须包含主键
# *无法成功，可能需要表中加主键
# Self.objects.raw('select * from stu_self')
# 不需要主键
# from django.db import connection
# cur=connection.cursor()
# cur.execute('select sname from stu_self')
# <django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x000001B50EB5B1C0>
# cur.fetchall()

# s=from stu.models import *
# 获得全部数据，循环输出
# for i in s:
#     print(i)
# from django.db.models import Q,F
# 不要将数据格式设置错误
# 与&或|非~    Q查询
# Self.objects.filter(Q(score=1.3)&Q(sname='tom'))
# Self.objects.filter(Q(score=2.8)|Q(sname='jary'))
# Self.objects.filter(~Q(sname='jary'))
# F查询
# 查询字段、更新数值
# Self.objects.filter(id=2).update(score=F('score')+5)
#
# 数据库的事物
# A（原子性）C（一致性）I（隔离性）D（持久性）
# Serializable (串行化):可遗免脏读、不可重复读、幻读发生
# Repeatable read (可重复读):可遗免脏读、不可重复读、（数据库默认级别）
# Read committed (读已提交):可遗免脏读
# Read uncommitted(读未提交):最低级别，任何情况都无法保证、,
# Django事务处理    原子性，事物回滚
# from django.db.transactioj import atomic
# @atomic

