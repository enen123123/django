import os.path

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Template,Context,loader
from django.views import View


def index(request):
    return None


class Index(View):
    def get(self,request):
        return render(request,'index.html')


def ren(request):
    # 使用中该渲染方式无法识别html的标准格式，
    with open(os.path.join(os.getcwd(),'templates','render.html'),'rb') as fr:
        contect=fr.read()
    # 创建模板对象
    t=Template(contect)
    c=Context({'uname': 'tom'})
    # 将参数传递给模板页面渲染，生成页面的字符串
    renderStr=t.render(c)
    return HttpResponse(renderStr)


def ren2(request):
    # 该渲染方式可以识别html
    t=loader.get_template('render.html')
    renderStr2=t.render({'uname':'tom'})
    return HttpResponse(renderStr2)


def ren3(request):
    # 该渲染方式也可以识别html
    return render(request,'render.html',{'uname':'tom'})


def tem(request):
    # 新建templates查找文件默认优先在根目录下查找，然后在其他应用包下查找
    return render(request,'tem.html')