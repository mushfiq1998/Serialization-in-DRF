from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    institute = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

