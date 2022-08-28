
from django.shortcuts import render

# Create your views here.
from movie.models import Movie

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

import math
#
# def page_movie(num,size=3):
# #分页
# #     判断是否越界
#     if num<1:
#         num=1;
#     # 总记录数
#     totalrecords=Movie.objects.all().count();
#     totalpages=int(math.ceil(totalrecords*1.0/size));
#     if num>totalpages:
#         num=totalpages;
# #     获取当前页数据
#     mlist=Movie.objects.all()[((num-1)*size):num*size];
#     return mlist;

def index_view(request):

    # num=int(request.GET.get('num',1));
    # # 获取Movie表中的所有数据

    # movielist = Movie.objects.all();
    # # 分页
    # movielist=page_movie(num);
    #
    # previous_page=num-1;
    # next_page=num+1;
    # return render(request,'index.html',{'movielist':movielist,'previous_page':previous_page,'next_page':next_page})

    # 获取页面参数，初始为1
    num = int(request.GET.get('num', 1));
    movielist = Movie.objects.all().order_by('id');
    # 分页对象      Django分页
    page_obj=Paginator(movielist,3);
    # 获取当前页的数据
    try:
        per_page_list = page_obj.page(num);
    except PageNotAnInteger:
        per_page_list=page_obj.page(1);
    except EmptyPage:
        per_page_list=page_obj.page(page_obj.num_pages);

    # 每页开始页码
    begin = (num - int(math.ceil(8.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 7
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end <= 7:
        begin = 1
    else:
        begin = end - 4

    pagelist = range(begin,end+1)

    return render(request,'index.html',{'movielist':per_page_list,'pagelist':pagelist,'currentnum':num})