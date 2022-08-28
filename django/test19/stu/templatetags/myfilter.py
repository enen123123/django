#coding=utf-8
from django import template
from django.template import Library
# markdown  setting模块
register=Library()
# 装饰器改过滤器
@register.filter
# 无参数过滤器
def md(value):
    import markdown
    return markdown.markdown(value)

@register.filter
# 有参数过滤器
def split1(value,args):
    start,end=args.split(',')
    value=value.encode('utf-8').decode('utf-8')
    return value[int(start):int(end)+1]

# templatetags  py包的名字必须是这个
# 自定义过滤器
