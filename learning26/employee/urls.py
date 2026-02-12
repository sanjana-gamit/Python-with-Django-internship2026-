from . import views
from django.urls import path

urlpatterns = [
    path('employeeList/',views.employeeList),
    path('employeeFilter/',views.employeeFilter),
    path('createEmployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
    path('createCourse/',views.createCourse),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
]