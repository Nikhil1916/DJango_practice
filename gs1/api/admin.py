from django.contrib import admin
from .models import Student, Classes

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['id','section','grade']