from django.shortcuts import render
from .serializers import DatetimeSerializer,GetSerializer
from .models import numberstowords
from rest_framework import generics
from rest_framework.response import Response
from num2words import num2words

# Create your views here.
class words(generics.GenericAPIView):
    serializer_class = DatetimeSerializer
    def post(self,request):
        x = numberstowords()
        x.amount = request.data.get('amount')
        x.currencys = num2words(x.amount)
        x.save()
        return Response(GetSerializer(x).data)



