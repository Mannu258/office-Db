from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    params = mojo.objects.all().order_by('Item_Code')
    try:
        if request.method=="POST":
            code = request.POST.get('code')
            print(code)
            params = mojo.objects.filter(Item_Code=code)
    except:
        params = mojo.objects.all().order_by('Item_Code')

    return render(request,'index.html',{'params':params})

def details(request,id):
    params = mojo.objects.filter(id=id)
    return render(request,'details.html',{'params':params})


