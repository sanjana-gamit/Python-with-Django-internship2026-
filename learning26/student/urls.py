from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("home/", views.studentHome, name="student_home"),
    path("dashboard/", views.studentDashboard, name="student_dashboard"),
    path("list/", views.studentList, name="student_list"),
    path("service/", views.studentService, name="student_service"),
    path("create/", views.createStudent, name="create_student"),
]