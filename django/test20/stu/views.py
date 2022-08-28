from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')


def index_view1(request):
    print('index_view1')
    return HttpResponse('hello world!!!')


# CSRF
def index_view2(request):
    return render(request,'index2.html')