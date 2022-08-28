from django.core.cache import caches
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from stu.models import Student
# 缓存数据存入
cacheobj=caches['default']
def cacheview(func):
    # 验证是否缓存
    def _wrapper(request,*args,**kwargs):
        data=cacheobj.get(request.path)
        if data:
            print('缓存中读取数据')
            return HttpResponse(data)
        print('数据库中读取数据')
        response=func(request,*args,**kwargs)
        print('设置缓存')
        cacheobj.set(request.path,response.content)
        return response
    return _wrapper
@cacheview
def indexview(request):
    stulist=Student.objects.all()
    return render(request,'index.html',{'stulist':stulist})
#
# redis需要安装django-redis模块
# 全栈缓存、redis数据库
# python console中将数据放入redis  引入模块、选择数据、放入数据、提取数据
# from django.core.cache import caches
# cacheobj=caches['redis']
# cacheobj.set('uname','jary')
# True  数据传输成功会显示true
# cacheobj.get('uname')
# red-cli 服务端   选择端口、查看数据、建立数据、得到key对应的内容、删除所有
# select 1
# keys *
# set hello python
# get hello
# flushall


# 局部缓存

# views层级缓存
# from django.views.decorators.cache import cache_page
# #单位秒
# @cache_page(60*15)
# def index_view( request):
#   stus = stu.objects.all()
#   return render(request,"index. html",{'stus':stus})

# 模板层级缓存
# {%load cache %}
# {[% cache 5 缓存名称%}#这里是缓存5秒
#   {% for stu in stus %}
#       <li>{{stu.sname}}</li>
#   {% endfor %}
# { %endcache %}