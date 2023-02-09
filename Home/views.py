from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User

# Create your views here.
def apex(request):
    return render(request,'apex.html')

def index(request):
    return render(request,'index.html')

def img(request):
    return render(request,'login.html')
def img1(request):
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

    