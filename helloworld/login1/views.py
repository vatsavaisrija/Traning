from rest_framework.response import Response
from .models import teacher
from .serializers import teacherserializer, loginserializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Register(generics.GenericAPIView):
    serializer_class = teacherserializer
    def post(self,request):
        p = teacherserializer(data=request.data)
        p.is_valid(raise_exception=True)
        a = p.save()
        return HttpResponse("You Have Registered")
        return Response(teacherserializer(a).data)
class Login(generics.GenericAPIView):
    serializer_class = loginserializer
    def post(self, request):
        name = request.data.get("Name")
        Password = request.data.get("password")
        g = teacher.objects.get(Name=name)
        print(name)
        if g.password == Password:
            return HttpResponse("Success")
        else:
            return HttpResponse("Please check the details")