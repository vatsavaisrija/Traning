from django.shortcuts import render
from .models import Decimalvalue
from .serializers import decimalvalueSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse

class value(generics.GenericAPIView):
    serializer_class = decimalvalueSerializer
    def post(self, request):
        d = decimalvalueSerializer(data=request.data)
        print(d)
        d.is_valid(raise_exception=True)
        d.save()
        return HttpResponse("Success")
        return Response(decimalvalueSerializer(d).data)