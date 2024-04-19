from django.shortcuts import render
from . models import *
from django.db.models import Q

# Create your views here.

def index(request):
    params = mojo.objects.all().order_by('Item_Code')
    try:
        if request.method=="POST":
            code = request.POST.get('code')
            # print(code)
            params = mojo.objects.filter(Q(Item_Code__icontains=code) | Q(Item_name__icontains=code))
    except:
        params = mojo.objects.all().order_by('Item_Code')

    return render(request,'index.html',{'params':params})

def details(request,id):
    params = mojo.objects.filter(id=id)
    return render(request,'details.html',{'params':params})



