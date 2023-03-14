from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    ret = render(request, '홈워크_django_01_hw01_p.txt')

    return ret