#from django.shortcuts import render
#from django.http import HttpResponse
#import json
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
#api_view decorator converts any request coming to the usersApi function
#as a json Api request 
@api_view()
def usersApi(request):
    users = [
        {
            "name": "Abhinav",
            "language": "Python"
        },
        {
            "name": "Pulkit",
            "language": "Perl"
        }
    ]
    #Response will convert above dictionary to json repsonse
    return Response(users)
