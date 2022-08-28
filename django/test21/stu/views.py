from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# 引入自定义的forms模块
from .forms import *

from django.contrib.auth import authenticate,login


def loginview(request):
    return None


class Loginview(View):
    def get(self,request):
        # 引入自定义的forms
        loginfrom=Loginform1()
        return render(request,'login.html',{'loginfrom':loginfrom})

    def post(self,request):
        # 引入自定义的forms
        loginfrom=Loginform1(request.POST)
        # 进行表单校验
        if loginfrom.is_valid():
            # 获得数据库数据auth_user  字典
            data=loginfrom.cleaned_data

            print(data)
            # 根据输入的用户名和密码在系统数据库查询
            user=authenticate(username=data['username'],password=data['password'])
            if user:
                login(request, user)
                return HttpResponse('登陆成功')
            else:
                return HttpResponse('登陆失败，请重新登录：')
                # 输入失败重新输入
                # return render(request, 'login.html', {'loginfrom': loginfrom})




class Registerview(View):
    def get(self, request):
        cls_from=Clazzform()
        stu_from=Studentform()
        return render(request,'register.html',{'cls_from':cls_from,'stu_from':stu_from})

    def post(self, request):
        # 创建表单类对象
        cls_from = Clazzform(request.POST)
        stu_from = Studentform(request.POST)
        # 表单校验
        if cls_from.is_valid()*stu_from.is_valid():
            # 插入数据并提交
            cls=cls_from.save(commit=True)
            # 有外键先不提交
            stu = stu_from.save(commit=False)
            stu.cls=cls
            stu.save()
            return HttpResponse('注册成功')
        else:
            # return HttpResponse('登陆失败，请重新登录：')
            return render(request, 'register.html', {'cls_from':cls_from,'stu_from':stu_from})










