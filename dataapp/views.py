from django.shortcuts import render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    try:
        if request.method == "POST":
            code = request.POST.get('code')
            params = mojo.objects.filter(Q(Item_Code__icontains=code) | Q(Item_name__icontains=code)).order_by('Item_Code')
        else:
            params = mojo.objects.all().order_by('Item_Code')
    except:
        params = mojo.objects.all().order_by('Item_Code')
    # Pagination
    paginator = Paginator(params, 25)  # Show 25 items per page.
    page_number = request.GET.get("page")
    params = paginator.get_page(page_number)

    return render(request, "index.html", {"params": params})

def details(request,id):
    params = mojo.objects.filter(id=id)
    return render(request,'details.html',{'params':params})



