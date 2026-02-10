from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
#python class

#parent class model
#create table student(studentName varchar(100))
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

#meta class
    class Meta:
        db_table = "student"
    
    def __str__(self):
        return self.studentName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"

hobbies =[("reading","reading"), ("Writing", "Writing"), ("Travel","Travel"), ("Music","Music")]
class StudentProfile(models.Model):
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    class Meta:
        db_table = "studentprofile"
    
    def __str__(self):
        return self.studentId.studentName

class StudentResult(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentMarks = models.IntegerField()
    studentGrade = models.CharField(max_length=10)
    studentStatus = models.BooleanField(default=True)    
    class Meta:
        db_table = "studentresult"

class StudentCourse(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentCourse = models.CharField(max_length=100)
    studentStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "studentcourse"

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    discount = models.IntegerField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName

class StudentIDCard(models.Model):
    studentId = models.OneToOneField(Student, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=20)
    issueDate = models.DateField()

    class Meta:
        db_table = "studentidcard"

class StudentParent(models.Model):
    studentId = models.OneToOneField(Student, on_delete=models.CASCADE)
    fatherName = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)

    class Meta:
        db_table = "studentparent"
  
class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)






    


    

