# from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .models import Student
from .Serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


# copy of gs3 but class based
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            stu = Student.objects.all()
            stu = StudentSerializer(stu, many=True)
            all_students = JSONRenderer().render(stu.data)
            return HttpResponse(all_students, content_type="application/json")
        else:
            error = JSONRenderer().render(serializer.errors)
            return HttpResponse(error, content_type="application/json")
        
    def put(self, request, *argsm ,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        # print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            # for partial update
            serializer = StudentSerializer(stu, data=python_data, partial=True)
            
            #for complete update
            # serializer = StudentSerializer(stu, data=python_data) 
            
            
            if serializer.is_valid():
                serializer.save()
                res = {
                    'msg': 'Data Updated'
                }
                return HttpResponse(JSONRenderer().render(res), content_type="application/json")
            else:
                error = JSONRenderer().render(serializer.errors)
                return HttpResponse(error, content_type="application/json")
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            # try: 
            # catch(Exception):
                
            Student.objects.get(id=id).delete()
            res = {
                'msg':'Record deleted'
            }
            # return HttpResponse(JSONRenderer().render(res), content_type="application/json")
            # other way to return json respnse
            return JsonResponse(res,safe=False)
        
        

# /**
# @csrf_exempt
# def student_api(request, pk=None):
#     # if request.method == 'GET':
        
#         # json_data = request.body
#         # as script of python not working so commmenting and using normal
#         # stream = io.BytesIO(json_data)
#         # python_data = JSONParser().parse(stream)
#         # id = python_data.get('id', None)
#         # id = pk
#         # if id is not None:
#         #     stu = Student.objects.get(id=id)
#         #     serializer = StudentSerializer(stu)
#         #     json_data = JSONRenderer().render(serializer.data)
#         #     return HttpResponse(json_data, content_type='application/json')
#         # else:
#         #     stu = Student.objects.all()
#         #     serializer = StudentSerializer(stu,many=True)
#         #     json_data = JSONRenderer().render(serializer.data)
#         #     return HttpResponse(json_data, content_type='application/json')
        
#     if request.method == 'POST':
#          json_data = request.body
#          stream = io.BytesIO(json_data)
#          python_data = JSONParser().parse(stream)
#          serializer = StudentSerializer(data=python_data)
#          if serializer.is_valid():
#              serializer.save()
#              stu = Student.objects.all()
#              stu = StudentSerializer(stu, many=True)
#              all_students = JSONRenderer().render(stu.data)
#              return HttpResponse(all_students, content_type="application/json")
#          else:
#              error = JSONRenderer().render(serializer.errors)
#              return HttpResponse(error, content_type="application/json")
#     elif request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         # print(id)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             # for partial update
#             serializer = StudentSerializer(stu, data=python_data, partial=True)
            
#             #for complete update
#             # serializer = StudentSerializer(stu, data=python_data) 
            
            
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {
#                     'msg': 'Data Updated'
#                 }
#                 return HttpResponse(JSONRenderer().render(res), content_type="application/json")
#             else:
#                 error = JSONRenderer().render(serializer.errors)
#                 return HttpResponse(error, content_type="application/json")
#     else:
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         if id is not None:
#             # try: 
#             # catch(Exception):
                
#             Student.objects.get(id=id).delete()
#             res = {
#                 'msg':'Record deleted'
#             }
#             # return HttpResponse(JSONRenderer().render(res), content_type="application/json")
#             # other way to return json respnse
#             return JsonResponse(res,safe=False)
# #    **/         
        
        
        

        
            
        
        