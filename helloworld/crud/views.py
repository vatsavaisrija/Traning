from django.shortcuts import render
from django.http import HttpResponse

from .models import employee


def verfication(request):
    msg = ''
    if request.method == "POST":
        aa=employee()
        aa.name = request.POST['name']
        aa.email = request.POST['email']
        aa.address = request.POST['address']
        aa.phone = request.POST.get('phone')
        aa.save()

        msg = 'Data is Recorded'
    return render(request,'index.html',{'message': msg})


def update(request, id):
    aa = employee.objects.get(id=id)

    if request.method == 'POST':
        aa.name = request.POST['name']
        aa.email = request.POST['email']
        aa.address = request.POST['address']
        aa.phone = request.POST['phone']
        aa.save()
        return HttpResponse("Data is Update")
    return render(request,'index.html',{'employee':aa})



def delete(request, id):
    r = employee.objects.get(id=id)
    print(r)
    r.delete()
    return HttpResponse("Success")
def read(request):
    r = employee.objects.all()
    return render(request,'read.html',{'employee':r})

# Create your views here.