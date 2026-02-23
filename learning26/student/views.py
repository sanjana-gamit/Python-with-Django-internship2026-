from django.shortcuts import render,redirect
from .models import Student
from services.models import Service
from services.forms import ServiceForm
# Create your views here.

def studentHome(request):
    return render(request,"studentHome.html")
def studentDashboard(request):
    student_data = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"students/studentDashboard.html",student_data)    
    #student/studentDashboard.html
    #folder/filename


def studentList(request):
    service = Service.objects.all()
    return render(request,"students/student_list.html",{"service":service})

def studentService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
        else:
            return render(request,"students/student_service.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"students/student_service.html",{"form":form})

def createStudent(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
        else:
            return render(request,"students/createStudent.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"students/createStudent.html",{"form":form})