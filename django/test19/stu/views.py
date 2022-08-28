import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    # 列表
    l=['a1','a2','a3']
    # 字典
    d={'k1':'b1','k2':'b2'}
    # 现有html格式，不能解析，为了安全
    str='<h1>hello</h1>'

    return render(request,'index.html',{'uname':'tom','l':l,'d':d,'today':datetime.datetime.today(),'str':str})


def f1(request):
    li=['a1','a2']
    sc = '<h3>hello</h3>'
    return render(request,'f1.html',{'num':'6','str':'abcd','str1':'EFG','li':li,'sc':sc})


def f2(request):
    str='###配置路由'
    str2='hello world'
    return render(request,'f2.html',{ 'str':str,'str2':str2 })