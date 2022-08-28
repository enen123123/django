from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def request_view(request):

    print(request)
    # < WSGIRequest: GET '/stu/' >
    m=request.method
    print('请求方式:%s' %m)
    p=request.path
    print('访问地址:%s' %p)
    s = request.scheme
    print('访问地址:%s' % s)
    m=request.META
    # print('报文头:%s'%m)
    # 间接获取主机
    print('Host:%s' % m['HTTP_HOST'])
    # 直接获取主机
    print(request.get_host())
    g=request.GET
    # url后加：？+内容
    print('获取请求信息:%s'%g)
    G=request.GET
    # 获取相应的属性内容
    print(G.get('uname'))
    print(G.getlist('fav'))



    return HttpResponse('hello')


def response_view(request):
    # content_type='text/html;chartset=utf-8  用来设置内容格式  加了没用
    response=HttpResponse('<h1>h1字体<h1>')
    # 增加响应头信息
    # 方式一
    response.__setitem__('hello','123')
    # 方式二
    response['name']='tom'
    # 方式三   不能更改自己设置的
    response.setdefault('Date','321')


    return response