# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models







class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    download_url = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        # 改变编码 ，提取信息
        return u"%s"%(self.name)

    # 模型类   全部代码写、运行在python console上

    # def showsql():    展示mysql函数的创建，可以用来查看某一步的sql写法
    #     from django.db import connection
    #     print(connection.queries[-1]['sql'])  上一步
    #
    # showsql()     mysql函数的调用

    # 表单查询
    # Movie.objects.get(id='4')        查询对象、
    # Movie.objects.first()             第一条
    # Movie.objects.last()              最后一条
    # Movie.objects.count()             总记录数
    # Movie.objects.all()             所有记录，加[m,n]可切割提取
    # Movie.objects.filter()             查询对象、列表、error返回空列表
    # Movie.objects.filter(name__startswith='诱惑')  查询关键字开头，区分大小写，__后加i可以忽略下划线
    # Movie.objects.filter(name__endswith='2019')   查询关键字结尾
    # Movie.objects.filter(name__contains='2')  查询关键字包含
    # Movie.objects.filter(name='诱惑2019')   查询全称
    # Movie.objects.filter(name__isnull=True)   查询空表
    # Movie.objects.filter(name='诱惑2019',id=7)  多条件查询
    # Movie.objects.order_by('id')  排序，升序
    # Movie.objects.order_by('-id') 降序
    # Movie.objects.filter(id__gt='9')  大于
    # Movie.objects.filter(id__gte='9') 大于等于
    # Movie.objects.filter(id__lt='9')  小于
    # Movie.objects.filter(id__lte='9')  小于等于
    # Movie.objects.filter(id__range=('5','12'))    5~12之间
    # Movie.objects.filter(id__in=('5','12'))   5或12

    # 增改删
    # t=Movie(id='15',name='百度',account='baidu',image='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png',download_url='http://mo.baidu.com/')
    # t.save()  先存储在提交，只有全部的内容才能成功，少一个都不行
    # Movie.objects.create(id='16',name='百度',account='baidu',image='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png',download_url='http://mo.baidu.com/')
    # 存储并保存数据
    # last=Movie.objects.last()     获取最后一个数据
    # last.name='百度1'   修改数据
    # last.save()   提交
    # Movie.objects.filter(name='百度1').update(name='百度2')   修改数据并提交
    # Movie.objects.filter(name__endswith='2').delete()   删除指定形式（以2结尾）的数据


    class Meta:
        managed = False
        db_table = 'movie'


