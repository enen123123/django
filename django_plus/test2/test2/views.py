# coding=utf-8

# 显示登陆首页
from django.http import HttpResponse
# 页面响应对象
from django.shortcuts import render


def login_view(request):
    return render(request,'login.html')

# 读取http文件
def tologin_view(request):
    # 获取输入框内容   获取请求参数
    uname=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    if uname=='张三' and pwd=='123456':
        return HttpResponse(u'登陆成功')

    return HttpResponse(u'登陆失败')

'''
    更改get(默认方式)为post：
        将所有的get更换为post，并加上解决方法
        请求地址+?+请求参数
        403   post错误码 
            解决方法1：{% csrf_token %}
            方法2：注释掉setting.py的MIDDLEWARE中的'django.middleware.csrf.CsrfViewMiddleware',
    
    http协议：超文本传输协议
    简单抓包：F12查看源代码->Network
    请求信息部分：
        请求行：请求方式、地址、协议类型和版本
        请求头：请求报文头信息
        空行：
        请求实体内容：get:空    post:post请求的请求参数
    相应信息部分：
        相应行、状态行：协议类型和版本、状态码及其相应的描述信息
        响应（报文）头：相应的报文头信息
        空行:
        相应实体内容：页面输出的内容
        
    get请求：
        1、<form method='get'></form>
        2.通过地址栏直接输入请求地址
        3.<a href="/login/?uname=张三&pwd=123456">超链接</a>
        4.<script> location.href="/login/?uname=张三&pwd=123456"</script>
    post请求：
        1、<form method='post'></form>
        
    get特点：
        1.将数据缓存在客户端，不需要再次从服务器获取
        2.请求参数存在于地址栏
        3.请求参数的大小受到限制
        4.不安全，密码会被容易获取
    post特点：
        1.无缓存，每次由数据库服务器获取
        2.请求参数存放在请求实体内容上
        3.文本限制较小
        4.相对安全
        
    http协议特点：
        1.单向性协议 先有请求才有相应
        2.无记忆功能 每次都要登录
            cookie:将数据保存在客户端
            session:将数据保存在服务器
        3.从http协议1.1之后支持长链接 只需要建立一次链接就能不断发送文件，不需要多次建立连接

        
'''