from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def index_view(request):
    return render(request,'register.html')


def regieter(request):
    # 获取请求参数
    sname=request.POST.get('sname','')
    spwd=request.POST.get('spwd','')

    # 将数据存入数据库
    student=Student(sname=sname,spwd=spwd)
    student.save()

    return HttpResponse('注册成功！！！')


def show(request):
    #查询学生表中的所有信息Queryset[]
    stuList=Student.objects.all()

    return render(request,'show.html',{'stuList':stuList})