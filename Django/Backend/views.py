from django.shortcuts import render
from rest_framework .response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from django .http import HttpResponse



class singup(generics.GenericAPIView):
    serializer_class = registerserializer


    def post(self,request):
        s = registerserializer(data=request.data)

        if s.is_valid(raise_exception=True):
            t = s.save()
            return Response({"Message":"Sussessful",
                             "result":registerserializer(t).data,
                             "Status" : 200})
        else:
            return Response({"Message":"Invalid Details",
                             "HasError": False,
                             "Status" : 400})


class login(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        t = register.objects.get(email=email)
        if t.password==password:

            return Response({"Message":"Sussessful",
                             "result": registerserializer(t).data,
                             "HasError": False,
                             "Status" : 200})

        else:
            return Response({"Message":"Invalid Details",
                             "HasError": False,
                             "Status" : 400})

class update(generics.GenericAPIView):
    serializer_class = registerserializer

    def put(self, request, id):
        a = register.objects.get(id=id)
        b = registerserializer(a, data=request.data, partial=True)
        if b.is_valid(raise_exception=True):
            x = b.save()
            return Response({"Message":"Sussessful",
                             "result":registerserializer(x).data,
                             "Status" : 200})
        else:
            return Response({"Message":"Invalid Details",
                             "HasError": False,
                             "Status" : 400})

# class update(generics.GenericAPIView):
#     serializer_class = registerserializer

#     def put(self, request, email):
#         a = register.objects.get(email=email)
#         b = registerserializer(a, data=request.data, partial=True)
#         if b.is_valid(raise_exception=True):
#             x = b.save()
#             return Response({"Message":"Sussessful",
#                              "result":registerserializer(x).data,
#                              "Status" : 200})
#         else:
#             return Response({"Message":"Invalid Details",
#                              "HasError": False,
#                              "Status" : 400})

class forgot(generics.GenericAPIView):
    serializer_class = forgetserializer

    def put(self,request,id):
        v = register.objects.get(id=id)
        g = forgetserializer(v,data=request.data)
        if g.is_valid(raise_exception=True):
            t = g.save()
            return Response({"Message":"Sussessful",
                             "result":forgetserializer(t).data,
                             "Status" : 200})
        else:
            return Response({"Message":"Invalid Details",
                             "HasError": False,
                             "Status" : 400})

class getall(generics.GenericAPIView):
    serializer_class = registerserializer

    def get(self,request):
        g = register.objects.all()
        f = registerserializer(g,many=True)
        return Response({"Message":"Sussessful",
                         "result":(f).data,
                         "Status" : 200})

class getbyid(generics.GenericAPIView):
    serializer_class = registerserializer

    def get(self,request,id):
        f = register.objects.get(id=id)
        return Response({"Message":"succes",
                         "result":registerserializer(f).data,
                         "Status" : 200})


class details(generics.GenericAPIView):
    serializer_class = campserializer

    def post(self,request):
        d = campserializer(data=request.data)
        if d.is_valid(raise_exception=True):
            g = d.save()
            return Response({"Message":"succes",
                             "result":campserializer(g).data,
                             "Status" : 200})
        else:
            return Response({"Message":"Invalid Details",
                             "HasError": False,
                             "Status" : 400})

class detailsupdate(generics.GenericAPIView):
    serializer_class = campserializer

    def put(self, request,id):
        a = camp.objects.get(id=id)
        b = campserializer(a, data=request.data, partial=True)
        if b.is_valid(raise_exception=True):
            x = b.save()
            return Response({"Message":"succes",
                             "result":campserializer(x).data,
                             "Status" : 200})
        else:
            return Response({"Message":"Invalid Details",
                             "HasError": False,
                             "Status" : 400})

class getdetailsbyid(generics.GenericAPIView):
    serializer_class = campserializer

    def get(self,request,user_details):
        f = camp.objects.filter(user_details=user_details)
        if f:
            x = campserializer(f, many=True)
            return Response({"Message": "succes",
                             "result": x.data,
                             "Status" : 200})
        else:
            return Response({
                "Message": "Child not found",
                "Status": 404
            })

class getalldetails(generics.GenericAPIView):
    serializer_class = campserializer

    def get(self,request):
        g = camp.objects.all()
        f = campserializer(g,many=True)
        return Response({"Message":"Sussessful",
                         "result":(f).data,
                         "Status" : 200})

class getbyskills(generics.GenericAPIView):
    serializer_class = skillserializer

    def get(self,request,skills):
        a = camp.objects.filter(skills=skills)
        if a:
            x = skillserializer(a , many=True)
            return Response({"Message":"succes",
                             "result": x.data,
                             "Status" : 200})
        else:
            return Response({
                "Message": "Child not found",
                "Status": 404
            })

class getbystream(generics.GenericAPIView):
    serializer_class = streamserializer

    def get(self, request, stream):
        a = camp.objects.filter(stream=stream)
        if a:
            x = streamserializer(a, many=True)
            return Response({"Message": "succes",
                             "result": x.data,
                             "Status": 200})
        else:
            return Response({
                "Message": "Child not found",
                "Status": 404
            })

class getbyyear(generics.GenericAPIView):
    serializer_class = yearserializer

    def get(self, request, year):
        a = camp.objects.filter(year=year)
        if a:
            x = yearserializer(a, many=True)
            return Response({"Message": "succes",
                             "result": x.data,
                             "Status": 200})
        else:
            return Response({
                "Message": "Child not found",
                "Status": 404
            })

class getbyscore(generics.GenericAPIView):
    serializer_class = scoreserializer

    def get(self, request, score):
        a = camp.objects.filter(score=score)
        if a:
            x = scoreserializer(a, many=True)
            return Response({"Message": "succes",
                             "result": x.data,
                             "Status": 200})
        else:
            return Response({
                "Message": "Child not found",
                "Status": 404
            })

class getbyemail(generics.GenericAPIView):
    serializer_class = registerserializer

    def get(self,request,email):
        f = register.objects.get(email=email)
        return Response({"Message":"succes",
                         "result":registerserializer(f).data,
                         "Status" : 200})