from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from product.models import CakePro
from django.http.response import JsonResponse

# Create your views here.
def apex(request):
    return render(request,'apex.html')

def index(request):
    data=CakePro.objects.all()
    if 'username' in request.COOKIES:
        x=request.COOKIES['username']
    else: 
            x=''
    return render(request,'index.html',{'data':data,'abc':x})

def log(request):
    if request.method=='POST':
        uname=request.POST["Username"]
        pword=request.POST["Password"]
        user=auth.authenticate(username=uname,password=pword)
        if(user is not None):
            auth.login(request,user)
            response=redirect('/')
            response.set_cookie('username',uname)
            return response
            
        else:
            msg="Invalid"
        
            return render(request,'login.html',{"mess":msg})
    else:
        return render(request,'login.html')


def reg(request):
    if request.method=='POST':
        uname=request.POST["Username"]
        fname=request.POST["Firstname"]
        lname=request.POST["Lastname"]
        Email=request.POST["EMail"]
        pword=request.POST["Password"]
        repword=request.POST["RePassword"]

        if pword==repword:
            if User.objects.filter(username=uname).exists():
                msg="Username already Taken"
            elif User.objects.filter(email=Email).exists():
                msg="E-mail already taken"
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=Email,password=pword)
                user.save()
                auth.login(request,user)        #Automatically login after registration
                msg="Registration successful"
                return redirect('/')
        else:
            msg="password not same"

            return render(request,'register.html',{'regs':msg})

    else:
         return render(request,'register.html')

def logsub(request):
    uname=request.POST["Username"]
    pword=request.POST["Password"]
    user=auth.authenticate(username=uname,password=pword)
    if(user is not None):
        auth.login(request,user)
        msg="Login Successful"
        return redirect('/')
    else:
        msg="Invalid"
        
        return render(request,'login.html',{"mess":msg})

def regsub(request):
    uname=request.POST["Username"]
    fname=request.POST["Firstname"]
    lname=request.POST["Lastname"]
    Email=request.POST["EMail"]
    pword=request.POST["Password"]
    repword=request.POST["RePassword"]

    if pword==repword:
        if User.objects.filter(username=uname).exists():
            msg="Username already Taken"
        elif User.objects.filter(email=Email).exists():
            msg="E-mail already taken"
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=Email,password=pword)
            user.save()
            auth.login(request,user)        #Automatically login after registration
            msg="Registration successful"
            return redirect('/')
    else:
        msg="password not same"

    return render(request,'register.html',{'regs':msg})

def logout(request):
    auth.logout(request)
    response=redirect('/')
    response.delete_cookie('username')
    return response

def search(request):
    return render(request,'search.html')
    
def autocom(request):
    if 'term' in request.GET:
        val=request.GET['term']
        names=CakePro.objects.filter(name__istartswith=val)
        print('hi',names)
        name=[]
        for i in names:
            name.append(i.name)
    return JsonResponse(name,safe=False)    #for not loading or refreshing give back the value as Jason response
    
