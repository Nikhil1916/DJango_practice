from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(null=False)
    city = models.CharField(max_length=100)