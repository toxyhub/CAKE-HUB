from django.shortcuts import render,redirect
from django.contrib.auth.models import auth

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
    uname=request.GET["Username"]
    pword=request.GET["Password"]
    user=auth.authenticate(username=uname,password=pword)
    if(user is not None):
        auth.login(request,user)
        msg="Login Successful"
        return redirect('/')
    else:
        msg="Invalid"
        
        return render(request,'apex.html',{"a":msg})