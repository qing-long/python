from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello world this is / page')


def django_index(request):
    return render(request, 'index.html')
