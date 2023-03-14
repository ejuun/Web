from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    ret = render(request, 'main.html')
    return ret

def profile(request):
    ret = render(request,'profile.html')
    return ret