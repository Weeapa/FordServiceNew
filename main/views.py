from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("<h1>Welcome to FordService<h1>")



def about(request):
    return HttpResponse("About")

