from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def query1_view(request):
    return HttpResponse('hello world')


def query2_view(request,num):
    return HttpResponse(num)


def query3_view(request,num3):
    return HttpResponse(num3)


def query4_view(request,hello):
    return HttpResponse(hello)


def query5_view(request):
    return HttpResponse('query5（通过query6找到）')

def query6_view(request):
    # return HttpResponseRedirect(reverse('q1'))
    return render(request,'query6.html')


