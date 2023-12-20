from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .Serializers import StudentSerializer
from rest_framework import status

# Create your views here.

# @api_view()
# def hello_world(request):
#     return Response({"msg":"Hello World"})

@api_view(['POST','GET','DELETE','PUT'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    if request.method == 'POST':
        print(request.data)
        headers = {"Content-Type": "application/json"}
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data)            
        else:
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        if request.data.get('id') is not None:
            id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated successfully"})
    if request.method == "DELETE":
        id = request.data.get("id")
        stu = Student.objects.get(id=id).delete()
        return Response({"msg":"Data Deleted successfully"})

            