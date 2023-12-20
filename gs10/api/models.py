from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(default=1)
    city = models.CharField(max_length=100)