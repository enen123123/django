#coding=utf-8
# 中间件提取
# from django.middleware.security import SecurityMiddleware
from django.utils.deprecation import MiddlewareMixin

# 访问请求的时候调用
class Row1(MiddlewareMixin):
    def process_request(self, request):
        print('处理请求')

#   'django.middleware.csrf.CsrfViewMiddleware',
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('视图函数')

    def process_response(self, request, response):
        print('处理相应')
        return response

class Row2(MiddlewareMixin):
    def process_request(self, request):
        print('处理请求2')

#   'django.middleware.csrf.CsrfViewMiddleware',
def process_view(self, request, callback, callback_args, callback_kwargs):
    print('视图函数')

    def process_response(self, request, response):
        print('处理响应2')
        return response

