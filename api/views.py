#from django.shortcuts import render
#from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
#from rest_framework.request import Request
from rest_framework.response import Response

from api import serializers
from api import models

#We have created this class just for example we will fetch
#data for serializers from models created
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

# Create your views here.
#api_view decorator converts any request coming to the usersApi function
#as a json Api request 
@api_view()
def usersApi(request):
    #users = [
     #   {
      #      "name": "Abhinav",
       #     "language": "Python"
        #},
        #{
        #    "name": "Pulkit",
        #    "language": "Perl"
        #}
    #]
    student1 = Student('Abhinav',1,100)
    student2 = Student('Pulkit',2,99)
    student3 = Student('Shubham',3,98)
    response = serializers.StudentSerializer([
        student1,
        student2,
        student3
    ],many=True)
    #Response will convert above dictionary to json repsonse
    return Response(response.data)


@api_view(['POST'])
def createArticleApi(request):
    body=request.data
    response = serializers.ArticleSerializer(data=body)
    if response.is_valid():
        inst=response.save()
        response = serializers.ArticleSerializer(inst)
        return Response(response.data)
    return Response(response.errors)

@api_view()
def articleApi(request):
    article = models.Article.objects.all()
    response = serializers.ArticleSerializer(article,many=True)
    return Response(response.data)
