from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student
from test13.settings import  MEDIA_ROOT


def upload(request):


    return render(request,'upload.html')


def toupload(request):
    # 获取请求参数
    sname=request.POST.get('sname')
    sfile=request.FILES.get('sfile')

    #     放入数据库
    student=Student.objects.create(sname=sname, sfile=sfile)
    # 判断信息传输成功
    if student:
        return HttpResponse('success')
    return HttpResponse('failed')


def showall(request):
    students=Student.objects.all()
    return render(request,'show.html',{'students':students})


def watch(request):
    # / images / try_03.png
    sfile=request.GET.get('sfile')
    # 获取文件名字
    sfilename=sfile[sfile.rindex('/')+1:]
    #获取文件存储位置
    import os
    filepath=os.path.join(MEDIA_ROOT,sfile)
    with open(filepath,'rb') as fr:
        content=fr.read()
    resource1=HttpResponse(content)
    # png图片解码
    resource1['content-type']='image/png'

    # resource1['content-disposition']='attachment;filename'+sfilename

    return resource1


def down(request):
    # / images / try_03.png
    sfile = request.GET.get('sfile')
    sfilename = sfile[sfile.rindex('/') + 1:]
    # 获取文件存储位置
    import os
    filepath = os.path.join(MEDIA_ROOT, sfile)
    with open(filepath, 'rb') as fr:
        content = fr.read()
    resource1 = HttpResponse(content)
    # # png图片解码
    # resource1['content-type'] = 'image/png'
    # 设置响应头信息实现附件下载功能
    resource1['content-disposition']='attachment;filename'+sfilename

    return resource1