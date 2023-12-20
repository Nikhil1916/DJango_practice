from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.db import models
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
    
#model object - Single Student data
def student_detail(request, pk):
    print(pk)
    stu  = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(serializer.data)
    json_data =  JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


 # Query Set - All student data
def student_list(request):
    stu  = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    print(serializer.data)
    json_data =  JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# add instance
@csrf_exempt
def student_create(request):
    print("post method")
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'data inserted'
            }
            json_data =  JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
            
        