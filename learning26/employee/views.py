from django.shortcuts import render, HttpResponse, redirect, render
from .models import Employee
from .forms import EmployeeForm,CourseForm

# Create your views here.
def employeeList(request):
   employees = Employee.objects.all().values()
   print(employees)
   return render(request, 'employee/employeeList.html',{"employees":employees})

def employeeFilter(request):
    employee = Employee.objects.filter(name ="Rohit").values()
    employee2 = Employee.objects.filter(post ="Vise president").values()
    employee3 = Employee.objects.filter(name ="Rohit",post ="Vise president").values()

    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

    #lt , lte

    #string queries
    employee6 = Employee.objects.filter(post__exact="HR").values()
    employee7 = Employee.objects.filter(post__iexact="Manager").values()
    #contains
    employee8 = Employee.objects.filter(name__contains="R").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

    #in
    employee14 = Employee.objects.filter(name__in=["Rohit","Samir"]).values()    

    #range
    employee15 = Employee.objects.filter(age__range=[24,30]).values()    

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc


    #and
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    print("query 18",employee18) 
    return render(request, 'employee/employeeFilter.html')

def createEmployee(request):
    name = "Ayaan"
    age = 21
    city = "Delhi"
    email = "ayaan@gmail.com"
    salary = 50000
    status = True
    post = "Manager"
    join_date = "2022-01-01"
    Employee.objects.create(name=name,age=age,city=city,email=email,salary=salary,status=status,post=post,join_date=join_date)
    
    return HttpResponse("Create Employee")

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employeeList") 
    else:
        form = EmployeeForm()
    return render(request, 'employee/createEmployeeWithForm.html', {'form': form})

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Course created successfully")
    else:
        form = CourseForm()
    return render(request, 'employee/createCourse.html', {'form': form})

def deleteEmployee(request,id):
   print("id from url =",id)
   Employee.objects.filter(id=id).delete()
   return redirect("employeeList")

def filterEmployee(request):
    print("filter employee called....")
    employees = Employee.objects.filter(age__gt=23).values()
    print("filter employee =",employees)
    return render(request, 'employee/employeeFilter.html', {'employees': employees})

def updateEmployee(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        form.save()
        return redirect("employee:employeeList")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/updateEmployee.html', {'form': form})

def sortemployeesAsc(request):
  employees = Employee.objects.order_by("age")
  return render(request, "employee/employeeList.html", {
    "employees": employees
  })

def sortemployeesDesc(request):
  employees = Employee.objects.order_by("-age")
  return render(request, "employee/employeeList.html", {
    "employees": employees
  })