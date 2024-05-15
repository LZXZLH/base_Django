from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python函数
视图函数有2个要求：
    1.视图函数的第一个参数就是接收请求,这个请求就是HTTP request 的类对象
    2.
    
"""
from django.http import HttpRequest
from django.http import HttpResponse
#我们期望用户输入 index 来访问视图函数
def index(request):

    return HttpResponse("ok")