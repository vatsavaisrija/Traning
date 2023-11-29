from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def house(request):
    return HttpResponse("HELLOWORLD")

def student(request):
    return HttpResponse("Welcome")
def members(request):
    return HttpResponse("New Members")
