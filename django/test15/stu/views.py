import base64

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def set_cookie(request):
    # cookie之中传值
    resp = HttpResponse()
    # 默认情况下cookie教据保在在浏览器的缓存(内存)
    # 设置cookie有效时间（max_age）,存在的对应域名（path）

    b = base64.b64encode('tom'.encode('utf-8'))
    # print(b)  编码会被破解
    resp.set_signed_cookie('uname',b,salt='加密盐',path='/111/')

    return resp


def get_cookie(request):
    # 获取缓存值
    # if request.COOKIES.has_key('uname'):  py2
    # 不需要path
    c=base64.b64encode('tom'.encode('utf-8'))
    print(c)
    uname=request.get_signed_cookie('uname',salt='加密盐')
    # u=base64.b64decode(uname).decode()
    return HttpResponse('value:%s'%uname)

    # if 'uname' in request.COOKIES:
    #     return HttpResponse(request.COOKIES['uname'])
    # else:
    #     return HttpResponse('hello')

# 编码    感觉会被破解
# import base64
# 加密
# base64.b64encode('hello'.encode('utf-8'))
# b'aGVsbG8='
# 解密
# base64.b64decode('aGVsbG8=').decode()
# 'hello'
