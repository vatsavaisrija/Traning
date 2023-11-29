from django.shortcuts import render
from rest_framework import generics
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import buyerserializer,resetserializer
from .models import buyer
from django.http import HttpResponse,JsonResponse


class create(generics.CreateAPIView):
    serializer_class = buyerserializer

    def post(self, request):
        v = buyerserializer(data=request.data)
        # print(v, "v sdfghjk")
        # v.ticketclass = request.data('ticketclass')
        # v.movie_name = request.data('movie_name')
        # v.theatre = request.data('theatre')
        # v.seat_no = request.data('seat_no')
        v.is_valid(raise_exception=True)
        a= v.save()

        msg = 'ticket was booked in your show'
        return Response({'msg': msg,
                         'result':buyerserializer(a).data})

# class GetApi(generics.RetrieveUpdateAPIView):
#     queryset = buyer.objects.all()
#     serializer_class = buyerserializer
#
# class UpdateApi(generics.RetrieveUpdateAPIView):
#     queryset = buyer.objects.all()
#     serializer_class = buyerserializer
#
# class DeleateApi(generics.RetrieveUpdateAPIView):
#     queryset = buyer.objects.all()
#     serializer_class = buyerserializer


class getbyid(generics.GenericAPIView):
    serializer_class = buyerserializer
    def get(self,request,id):
        a=buyer.objects.filter(id=id)
        b=buyerserializer(a,many=True)
        # msg = 'ticket was booked in your show'
        return Response({'result': b.data})

class updatebyid(generics.GenericAPIView):
    serializer_class = resetserializer

    def put(self, request, id):
        a = buyer.objects.get(id=id)
        ticketclass = request.data.get('ticketclass')
        movie_name = request.data.get('movie_name')
        theatre = request.data.get('theatre')
        seat_no = request.data.get('seat_no')
        data = {'ticketclass': ticketclass, 'movie_name': movie_name, 'theatre': theatre, 'seat_no':seat_no}
        aa = resetserializer(a, data=request.data)
        aa.is_valid(raise_exception=True)
        aa.save()

        return Response({'message': 'successful',
                             'Result': "success",
                             'HasError': False,
                             'status': 200})




class deletebyid(generics.GenericAPIView):
    serializer_class = buyerserializer
    def delete(self, request,id):
        a = buyer.objects.get(id=id)
        a.delete()
        return Response('delete sucessfull')