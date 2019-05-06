from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('hello world. you are in polls app index')


def polls(request):
    return HttpResponse('this is polls page')
