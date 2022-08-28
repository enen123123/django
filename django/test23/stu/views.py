from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stu.models import Menu


class Areaview(View):
    def get(self,request):
        return render(request,'area.html')


def getinfo(request):
    # 获取传递的id
    pid=request.GET.get('pid',-1)
    pid=int(pid)
    # 将数据库数据提取过滤
    arealist=Menu.objects.filter(parentid=pid)
    jarealist=serializers.serialize('json',arealist)
    # 返回数据列表
    return JsonResponse({'jarealist':jarealist})