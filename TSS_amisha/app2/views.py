from django.shortcuts import render
from app1.models import Employee
from django.shortcuts import redirect

# Create your views here

def edit(request,pk):
    eddit=Employee.objects.get(id=pk)
    return render(request,'update.html',{'eddit':eddit})


def update(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method=='POST':
        employee.Name=request.POST.get('Name')
        employee.Email=request.POST.get('Email')
        employee.Photo=request.POST.get('Photo')
        employee.Contact=request.POST.get('Contact')
        employee.save()
        msg="data updated"
    return render(request,'update.html',{'employee':employee})

def delete(request,pk):
    sdel=Employee.objects.get(id=pk)
    sdel.delete()
    msg="data deleted"
    return redirect('showdata')


