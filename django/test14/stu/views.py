from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # 获取请求参数
        # 获取属性，如果获取不到得到空字符串
        uname=request.POST.get('uname','')
        pwd=request.POST.get('pwd','')
        # 判断属性是否正确
        if uname=='tom' and pwd=='123':
            # 重定向HttpResponseRedirect(第一种)、redirect（第二种，更高阶）
            #  302 临时重定向  再通过location来获取二次地址
            # return HttpResponseRedirect('https://www.baidu.com/')
            # return redirect('https://ai.taobao.com/')
            # 301 永久重定向     加参数将302改为301
            # return redirect('https://ai.taobao.com/',permanent=True)
            # 改变302\301
            # 修改状态码，响应头以重定向（第三种）
            resp=HttpResponse()
            resp.status_code=302
            resp.setdefault('Location','https://diannao.jd.com/')
            return resp
    # 301永久性重定向:搜索引擎会将重定向之后的新地址和网页数据缓存下来.
    # 302临时性重定向:搜索引擎只会讲页面数据缓存下，只会缓存旧地址


    return HttpResponseRedirect('/stu/login/')



