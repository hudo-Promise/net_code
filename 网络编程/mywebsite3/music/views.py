from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list(request):
    return HttpResponse('music里的list被调用')
