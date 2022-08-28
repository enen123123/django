from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    # 读取cookie中保存正确的值
    if 'user' in request.COOKIES:
        user=request.COOKIES.get('user')
        us=user.split(',')
        uname=us[0]
        pwd=us[1]
        return render(request,'login.html',{'uname':uname,'pwd':pwd})
    return render(request, 'login.html')

def tologin(request):
    uname=request.POST.get('uname','')
    pwd = request.POST.get('pwd', '')
    flag = request.POST.get('flag', '')
    # 判断登录成功
    resp=HttpResponse()
    if uname=='tom' and pwd=='123':
        resp.content=u'success!!!'
        if flag=='1':
            resp.set_cookie('user',uname+','+pwd,max_age=3600,path='/stu/login/')
            return resp
        else:
            resp.delete_cookie('user',path='/stu/tologin/')
            return resp
    else:
        resp.delete_cookie('user', path='/stu/tologin/')
        resp.status_code=302
        resp.setdefault('Location','https://www.baidu.com/')
        return resp