from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .Serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# @api_view()
# def hello_world(request):
#     return Response({"msg":"Hello World"})

class StudentView(APIView):
    
    # for basic authentication
    # authentication_classes = [BasicAuthentication]
    
    
    # for session authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None ,format=None):
        print(request)
        # return Response({"data":request})
        id = pk
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except AttributeError:
                print("ok")
                raise Response({"error":"INVALID_STUDENT_ID","msg": "STUDENT does not exist !"},
                                         status=status.HTTP_404_NOT_FOUND)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
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
    
    def put(self, request, pk=None ,format=None):
        if pk is not None:
            id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated successfully"})
    
    def patch(self, request, pk=None ,format=None):
        if pk is not None:
            id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated successfully"})
    
    def delete(self,request, pk=None):
        id = pk
        Student.objects.get(id=id).delete()
        return Response({"msg":"Data Deleted successfully"})
    