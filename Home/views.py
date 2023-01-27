from django.shortcuts import render

# Create your views here.
def apex(request):
    return render(request,'apex.html')

def index(request):
    return render(request,'index.html')