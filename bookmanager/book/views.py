from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python函数
视图函数有2个要求：
    1.视图函数的第一个参数就是接收请求,这个请求就是HTTP request 的类对象
    2.必须返回一个响应
    
"""
from django.http import HttpRequest
from django.http import HttpResponse
#我们期望用户输入 index 来访问视图函数
def index(request):
    context={
        'name':'zhangsan',
        'age':18,
        'hobby':['football','basketball']
    }
    # return HttpResponse("ok")
    return render(request,'book/index.html',context=context)