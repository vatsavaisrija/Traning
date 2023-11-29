from django.shortcuts import render
from rest_framework import generics
from.models import*
from rest_framework.response import Response
from.serializers import from1serializer, from2serializer, from3serializer
from django .http import HttpResponse
class funone(generics.GenericAPIView):
    serializer_class = from1serializer
    def post(self,request,*args, **kwargs):
        a = from1serializer(data=request.data)
        a.is_valid()
        user = a.save()
        return HttpResponse("Recorded")
        return Response(from1serializer(user).data)


class funtwo(generics.GenericAPIView):
    serializer_class = from2serializer
    def post(self,request,*args, **kwargs):
        b = from2serializer(data=request.data)
        b.is_valid(raise_exception=True)
        user = b.save()
        return HttpResponse("Recorded")
        return Response(from2serializer(user).data)


class funthree(generics.GenericAPIView):
    serializer_class = from3serializer
    def post(self,request,*args, **kwargs):
        c =from3serializer(data=request.data)
        c.is_valid(raise_exception=True)
        user=c.save()
        return HttpResponse("Recorded")
        return Response(from3serializer(user).data)


class GetModel(generics.GenericAPIView):
    queryset=from2serializer,from3serializer
    def get(self,request):
        m = person3.objects.all()
        s = person2.objects.all()
        details = person1.objects.all()
        serializer = from3serializer(m,many=True)
        serializers = from2serializer(s,many=True)
        ver = from1serializer(details,many=True)
        return Response(ver.data)
