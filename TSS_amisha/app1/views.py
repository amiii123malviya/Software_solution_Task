from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')

def register(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    photo=request.POST.get('image')
    password=request.POST.get('password')
    data=Employee.objects.filter(Email=email)
    print(data)

    if data:
        msg='email already exist'
        return render(request,'home.html',{'key':msg})
    else:
        Employee.objects.create(Name=name,
                                Email=email,
                                Photo=photo,
                                Contact=contact,
                                Password=password)
        # mmsg='suuccess'
        return render(request,'home.html')
    
def showdata(request):
    ddata=Employee.objects.all()
    data={
        'ddata':ddata
    }
    return render(request,'showdata.html',data)