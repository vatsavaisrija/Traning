from django.shortcuts import render,HttpResponse
from .serializers import CompanySerializer, employeeSerializer, emp1Serializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Company, employ

# Create your views here.

class CompanyAPI(generics.GenericAPIView):
   serializer_class= CompanySerializer

   def post(self, request):
      serializer=CompanySerializer(data=request.data)
      serializer.is_valid()
      user=serializer.save()
      return HttpResponse("Recorded")
      return Response(CompanySerializer(user).data)

class employeeAPI(generics.GenericAPIView):
   serializer_class= employeeSerializer

   def post(self, request):
      serializer=employeeSerializer(data=request.data)
      print(serializer)
      serializer.is_valid()
      user=serializer.save()
      return HttpResponse("Recorded")
      return Response(employeeSerializer(user).data)

class employee1API(generics.GenericAPIView):
   serializer_class = emp1Serializer

   def post(self,request, *args, **kargs):
      serializer=emp1Serializer(data=request.data)
      print(serializer)
      serializer.is_valid(raise_exception=True)
      user =serializer.save()
      return HttpResponse("Recorded")
      return Response(emp1Serializer(user).data)