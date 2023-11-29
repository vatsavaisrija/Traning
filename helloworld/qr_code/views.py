from django.http import HttpResponse
from django.shortcuts import render
from pyqrcode import *
from rest_framework.response import Response
from .models import folder, qrimage
from .serializers import folderSerializer
from rest_framework import generics
import base64
import png

class home(generics.GenericAPIView):
    serializer_class = folderSerializer

    def post(self, request):
        item_name = request.data.get('item_name')
        print(item_name)
        item_address = request.data.get('item_address')
        print(item_address)
        a = item_name+item_address
        b = pyqrcode.create(a)
        print(b)

#just to know to wether we can use serilizers and templates at a time but this is not main

        b.png('b.png', scale=7)
        byteform = ""
        with open('b.png', 'rb') as imagefile:
            byteform = base64.b64encode(imagefile.read())
            print(byteform)
        # user=code.objects.create(FirstName=FirstName,Age=Age,Qrcode=byteform)
        qrdb = folder()
        qrdb.item_name = item_name
        qrdb.item_address = item_address
        qrdb.item_code = byteform
        qrdb.save()
        return Response(folderSerializer(qrdb).data)

def upload(request):
    if request.method == 'POST':
        b = qrimage()
        b.name = request.POST.get("name")
        b.image = request.FILES['image']
        print(b.image)
        b.save()
        return HttpResponse('success')
    return render(request, 'codeimage.html')


