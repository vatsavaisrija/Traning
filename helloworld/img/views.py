from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import Img
from .form import ImgForm


def index(request):
    if request.method == "POST":
        form = ImgForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse('successfully')
    return render(request, 'imgread.html')


def table(request):
    a = Img.objects.all()
    return render(request, 'imageget.html', {'Img': a})