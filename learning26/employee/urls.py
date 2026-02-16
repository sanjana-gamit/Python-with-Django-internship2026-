from . import views
from django.urls import path

app_name = "employee"

urlpatterns = [

    path('list/',views.employeeList,name="employeeList"),
    path('filter/',views.employeeFilter,name="employeeFilter"),
    path('create/',views.createEmployee),
    path('createForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
    path('createCourse/',views.createCourse,name="createCourse"),
    path("delete/<int:id>",views.deleteEmployee,name="deleteEmployee"),
    path("update/<int:id>",views.updateEmployee,name="updateEmployee"),
    path("sortemployeesAsc/",views.sortemployeesAsc,name="sortemployeesAsc"),
    path("sortemployeesDesc/",views.sortemployeesDesc,name="sortemployeesDesc"),
]