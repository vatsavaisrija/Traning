from .models import resetpassword
from .serializers import registerserializer, logserializer, reseterserializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.

class registerAPI(generics.GenericAPIView):
    serializer_class = registerserializer
    def post(self,request):
        x = resetpassword()
        x.name = request.data.get('name')
        x.email = request.data.get('email')
        x.password = request.data.get('password')
        x.confirm_password = request.data.get('confirm_password')
        x.save()
        return HttpResponse('Successfully Registered')

class loginAPI(generics.GenericAPIView):
    serializer_class = logserializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        x = resetpassword.objects.get(email=email)
        if password == x.password:
            return HttpResponse('LoggedIn Successfully')
        else:
            return HttpResponse('Check your username / password')

class resetAPI(generics.GenericAPIView):
    serializer_class = reseterserializer

    def put(self,request,id):
        x = resetpassword.objects.get(id=id)
        y = reseterserializer(x, data=request.data,partial=True)
        y.is_valid(raise_exception=True)
        y.save()
        return HttpResponse('Successfully Changed')
        return Response(reseterserializer(y).data)
