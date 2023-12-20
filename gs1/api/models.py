from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100, default='India')
    
    
class Classes(models.Model):
    section = models.CharField(max_length=100),
    grade = models.CharField(max_length=100)
