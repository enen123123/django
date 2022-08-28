import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stu.models import Student


def getAjax(request):
    # 请求 type=xhr可以证明是ajax请求
    return render(request,'getajax.html')


def getview(request):
   uname=request.GET.get('uname','hello')
   print(uname)
   time.sleep(3)
   return JsonResponse({'flag':True})


def postview(request):
    uname = request.POST.get('uname', 'hello')
    print(uname)
    time.sleep(3)
    return JsonResponse({'flag': False})


class Onlyview(View):
    def get(self,request):
        return render(request,'only.html')


def getinfo(request):
    # 获取请求参数
    sname=request.GET.get('sname','')
    # 判断
    stu=Student.objects.filter(sname=sname)
    # flag=False
    if stu:
        flag=True
    else:
        flag=False

    return JsonResponse({'flag':flag})