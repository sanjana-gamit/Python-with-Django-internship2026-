from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    salary = models.IntegerField()
    status = models.BooleanField(default=True)
    post = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    

    class Meta:
        db_table = "employee"
    
    def __str__(self):
        return self.name
