from django.shortcuts import render,redirect
from product.models import CakePro ,commentBox 

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
    comment=commentBox.objects.create(user=user,comment=cmt,pro_id=pro)        # ORM inserting command in sql
    comment.save();
    return redirect('/pro/?id='+pro)
    #return render(request,'apex.html')
