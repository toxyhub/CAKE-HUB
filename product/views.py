from django.shortcuts import render,redirect
from product.models import CakePro ,commentBox 

# Create your views here.

def product(request):
    return render(request,'apex.html')

def details(request):
    idm=request.GET['id']
    data=CakePro.objects.get(id=idm)    #id is the database id compare with idm to take the product.
    if 'recent_view' in request.session:
        if idm in request.session['recent_view']:
            request.session['recent_view'].remove(idm)
        
        if len (request.session['recent_view'])>4:
            request.session['recent_view'].pop()
        print('hi',request.session['recent_view'])
        recent=[]
        for i in request.session['recent_view']:
            recent.append(CakePro.objects.get(id=i))
        request.session ['recent_view'].insert(0,idm)
        request.session.modified=True

        return render(request,'product.html',{'prodetail':data,'recent':recent})
        
        #img1=CakePro.objects.filter(id__in=request.session['recent_view'])
        #print('helloooo',img1)

    else:
        request.session['recent_view']=[idm]      #its the list method for creating empty list
        request.session.modified=True

    request.session.modified=True
    
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
