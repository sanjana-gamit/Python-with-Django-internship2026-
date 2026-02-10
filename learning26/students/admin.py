from django.contrib import admin
from .models import Student,Product,StudentResult,StudentCourse, StudentProfile, Category,Service

# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(StudentResult)
admin.site.register(StudentCourse)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)

