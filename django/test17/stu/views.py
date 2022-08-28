import json
import pickle

import jsonpickle
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views import View


def setsession(request):
    # 获取session，字典，放置在数据库django_session
    request.session['uname']='tom'
    # 设置数据存储时间
    request.session.set_expiry(3600)
    #

    return HttpResponse('hello')


def getsession(request):
    # 获取session数据
    uname=request.session.get('uname','')
    # 获取session的id
    print(request.session.session_key)
    return HttpResponse(uname)

class User(object):
    def __init__(self,uname,pwd):
        self.uname=uname
        self.pwd=pwd



def login(request):

    if request.method=='GET':
        return render(request,'login.html')
    else:
        # 获取请求参数
        uname=request.POST.get('uname','')
        pwd=request.POST.get('pwd','')
        if uname=='tom' and pwd=='123':
            # request.session['uname']=uname
            user=User(uname, pwd)
# import json
# import pickle     这两个自带，其他用法，有点类似，但谨慎
# import jsonpickle     需要setting下载包，将json（反）序列化，可读来获取
# 为了能够将多个数据传递jsonpickle.dumps、jsonpickle.loads(user)
            request.session['user'] = jsonpickle.dumps(user)
            return redirect('/stu/main/')
        else:
            return redirect('/stu/login/')


def main(request):
    # 获取用户名
    # uname=request.session.get('uname','')
    user=request.session.get('user','')
    if user:
        u=jsonpickle.loads(user)


    return HttpResponse(u'欢迎登陆,%s' % u.uname)
    # return HttpResponse(u'欢迎登陆,%s'%uname)


class Indexview(View):
    def get(self,request):
        return HttpResponse('hello class get')
    def post(self,request):
        # 只有表单可以post
        return HttpResponse('hello class post')

# 405代表表单中没有处理相应方式（GET\POST）的类或者函数
