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

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"


class StudentResult(models.Model):
    studentId = models.IntegerField()
    studentName = models.CharField(max_length=100)
    studentMarks = models.IntegerField()
    studentGrade = models.CharField(max_length=10)
    studentStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "studentresult"

class StudentCourse(models.Model):
    studentId = models.IntegerField()
    studentName = models.CharField(max_length=100)
    studentCourse = models.CharField(max_length=100)
    studentStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "studentcourse"
    


    

