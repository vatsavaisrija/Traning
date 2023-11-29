from .models import send
from .serializers import sendserializer
from rest_framework import generics
import base64
from .scan import generate
from rest_framework .response import Response




class create(generics.GenericAPIView):
    serializer_class = sendserializer

    def post(self, request):
        iteam_name = request.data.get('iteam_name')
        print(iteam_name)
        iteam_code = request.data.get('iteam_code')
        print(iteam_code)
        a = iteam_name + iteam_code
        combined = generate(a)
        print(combined)

        # b.img('b.img', scale=7)
        # byteform = ""
        # with open(b, 'rb') as img:
        #     byteform = base64.b64encode(img.read())
        #     print(byteform)
        # # user=code.objects.create(FirstName=FirstName,Age=Age,Qrcode=byteform)
        # qrdb = send()
        # qrdb.iteam_name = iteam_name
        # qrdb.iteam_code = iteam_code
        # qrdb.bar_code = byteform
        # qrdb.save()
        # return Response(sendserializer(qrdb).data)
        with open(combined, 'rb') as img:
            encoded = base64.b64encode(img.read())
            print(encoded)
            user = send.objects.create(iteam_name=iteam_name, iteam_code=iteam_code, bar_code=generate)
            print(user)
            user.save()
            return user



