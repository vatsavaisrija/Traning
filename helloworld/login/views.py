from django.shortcuts import render
from django.http import HttpResponse
from .models import employe


def register(request):
    if request.method == 'POST':
        x = employe()
        x.name = request.POST.get("name")
        x.email = request.POST.get("email")
        x.address =request.POST.get("address")
        x.phone = request.POST.get("number")
        x.password = request.POST.get("password")

        x.save()
        return HttpResponse("successful")
    else:
        return render(request, 'registration.html')
def singin(request):
    if request.method=="POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        g = employe.objects.get(name=name)
        if g.password == password:
            return HttpResponse("login sucessfully")
        else:
            return HttpResponse("invalid details")
    return render(request,"login.html")