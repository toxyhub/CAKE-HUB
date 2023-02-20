from django.shortcuts import render
from product.models import CakePro

# Create your views here.

def product(request):
    return render(request,'apex.html')

def details(request):
    idm=request.GET['id']
    data=CakePro.objects.get(id=idm)
    
    #return render(request,'post.html',{"prodetail":data})
    return render(request,'product.html',{"prodetail":data})

def commentarea(request):
    cmt=request.GET['cmt']
    user=request.GET['user']
    pro=request.GET['pro']
    print('hi',cmt,user,pro)
    return render(request,'apex.html')
