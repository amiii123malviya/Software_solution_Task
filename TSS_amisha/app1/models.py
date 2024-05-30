from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=250)
    Email=models.EmailField()
    Photo=models.ImageField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=250)


    class Meta():
        db_table="Employee"
        verbose_name_plural="Employee"
