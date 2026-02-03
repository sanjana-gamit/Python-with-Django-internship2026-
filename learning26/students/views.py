from django.shortcuts import render

from learning26 import students


# Create your views here.
def studentHome(request):
    return render(request, "studentHome.html")

def studentDashboard(request):
    student = { "name": "Alice", "age": 21, "city": "New York"}
    return render(request, "students/studentDashboard.html", student)

def DisplayStudentInfo(request):
    student_info = {
        "name": "John Doe",
        "age": 22,
        "city": "Los Angeles",
        "course": "B.Tech",
        "enrollment_number": "123456",
        "year": "2024",
        "major": "Computer Science",
        "university": "XYZ University"

    }
    return render(request, "students/studentInfo.html", student_info)
