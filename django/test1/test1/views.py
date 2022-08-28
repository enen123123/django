#coding=utf-8
from django.http import HttpResponse

# Alt+enter 调用模块
def index_view(request):
    return HttpResponse('hello world!!!')