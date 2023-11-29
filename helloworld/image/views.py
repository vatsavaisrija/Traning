from django.shortcuts import render,HttpResponse
from .models import Image64
from .form import im

# Create your views here.


def base64(request):
    if request.method == "POST":
        v = Image64()
        img = request.POST.get('image')
        v.images = im(img)
        print(v.images)
        v.save()
        return HttpResponse('successfully')
    return render(request,'image.html')