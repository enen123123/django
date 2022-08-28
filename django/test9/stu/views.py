from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import insertstu, Clazz


def register(request):
    return render(request,'register.html')


def addstu(request):
    # 获取请求参数
    sname = request.POST.get('sname')
    cname = request.POST.get('cname')
    coursenames = request.POST.getlist('coursename')

    # print(sname,cname)
    # print(coursename)

    # 将获取的数据插入到数据库中
    flag=insertstu(sname,cname,coursenames)
    if flag:
        return HttpResponse('success!!!')
    return HttpResponse('failed~~~')


def showall(request):
    # 擦汗寻所有的班级信息
    clslist=Clazz.objects.all()
    return render(request,'show.html',{'clslist':clslist})


def detail(request):
    # 查找班级下学生信息
    cno=request.GET.get('cno',-1)
    # 通过班级表查询学生信息
    stulist=Clazz.objects.get(cno=cno).student_set.all()
    return render(request,'detail.html',{'stulist':stulist})