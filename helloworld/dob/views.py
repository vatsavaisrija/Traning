from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response


class reverse(generics.GenericAPIView):
    serializer_class = convertserializer

    def post(self, request, *args, **kwargs):
        date = request.data.get("dob")
        print(date)
        form = converterserializer(data=request.data)
        print(form)
        form.is_valid()
        user = form.save()
        return Response(dateserializer(user).data)

