from django.http import HttpResponse
from django.http import request
from django.shortcuts import render

def index(request):
    html ="<html><body>Hello</html></body>"
    return HttpResponse(html)

def welcome(request):
    html ="<html><body>Welcome to Django.</html></body>"
    return HttpResponse(html)

def template_test(request):
    return render(request, 'test.html')

def template_test2(request):
    return render(request, 'test2.html')