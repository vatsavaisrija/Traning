from django.shortcuts import render, HttpResponse
from .serializers import *
from rest_framework import generics
from .models import apply
from rest_framework.response import Response
from rest_framework .views import APIView
# Create your views here.

class userregistrationview(generics.GenericAPIView):
    serializer_class = userregisterserializer

    def post(self, request):
        v = userregisterserializer(data=request.data)
        print(v)
        if v.is_valid():
            m=v.save()
            print(m)
            return Response({"message": "success",
                         "result": userregisterserializer(m).data,
                         "status": 200})
        else:
            return Response({"message": "invalid",
                         "result":False,
                         "status": 400})



class userRegisterAPI(generics.GenericAPIView):
    serializer_class = someserializer
    def post(self,request):
        vv = someserializer(data=request.data)
        print(vv)
        vv.is_valid(raise_exception=True)
        x=vv.save()
        print(x)
        # return HttpResponse("sucessfully")
        return Response(someserializer(x).data)


class updatebyid(generics.GenericAPIView):
    serializer_class = userregisterserializer

    def put(self,request,id):
        g = apply.objects.get(id=id)
        vv = userregisterserializer(g, data=request.data)
        vv.is_valid(raise_exception=True)
        f=vv.save()
        # return HttpResponse('successfully updated')
        return Response(userregisterserializer(f).data)


class getbyid(generics.GenericAPIView):
    serializer_class = userregisterserializer

    def get(self,request,id):
        print(id)
        v = apply.objects.get(id=id)
        return Response({"message": "success",
                         "result": userregisterserializer(v).data,
                         "status": 200})


class getall(generics.GenericAPIView):
    serializer_class = userregisterserializer

    def get(self,request):
        r = apply.objects.all()
        b=userregisterserializer(r,many=True)
        return Response({"result":b.data})

